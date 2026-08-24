"""Minimal Agent OS API entry point for Phase 1."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent_os.contracts import ExecutionMode, ExecutionRequest, RiskCheckRequest
from agent_os.execution import PaperExecutor
from agent_os.risk import AgentRiskGate
from agent_os.runtime import AgentGraph, draft_from_prompt


class DraftRequest(BaseModel):
    prompt: str = Field(min_length=1)
    name: str = Field(default="prompt-draft", min_length=1)


class RiskRequest(BaseModel):
    request_id: str = Field(min_length=1)
    idempotency_key: str = Field(min_length=1)
    actor_id: str = Field(min_length=1)
    symbol: str = Field(min_length=1)
    side: str = Field(min_length=1)
    quantity: float = Field(gt=0)
    price: float = Field(gt=0)
    leverage: int = Field(gt=0)
    mode: str = "paper"
    connector_id: str = "paper"
    reduce_only: bool = False


class PaperOrderRequest(RiskRequest):
    pass


app = FastAPI(
    title="CoinScopeAI Agent OS",
    version="0.1.0-phase1",
    description="Draft, inspect, risk-check, and paper-simulate strategies. Live execution is disabled.",
)

_gate = AgentRiskGate()
_executor = PaperExecutor(_gate)
_drafts: dict[str, dict[str, Any]] = {}


def _mode(value: str) -> ExecutionMode:
    try:
        return ExecutionMode(value.lower())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=f"Unsupported execution mode: {value}") from exc


def _risk_request(request: RiskRequest) -> RiskCheckRequest:
    return RiskCheckRequest(
        request_id=request.request_id,
        idempotency_key=request.idempotency_key,
        actor_id=request.actor_id,
        symbol=request.symbol.upper(),
        side=request.side.upper(),
        quantity=request.quantity,
        price=request.price,
        leverage=request.leverage,
        mode=_mode(request.mode),
        connector_id=request.connector_id,
        reduce_only=request.reduce_only,
    )


@app.get("/health")
def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": "agent-os-api",
        "phase": 1,
        "execution_mode": "paper",
        "live_order_placement": False,
        "mainnet_wallets": False,
    }


@app.post("/agent/drafts")
def create_draft(request: DraftRequest) -> dict[str, Any]:
    document = draft_from_prompt(request.prompt, request.name)
    graph = AgentGraph(document)
    response = {
        "document": document.to_dict(),
        "graph": graph.validate().to_dict(),
        "graph_nodes": graph.summary(),
    }
    _drafts[request.name] = response
    return response


@app.get("/agent/drafts/{name}")
def get_draft(name: str) -> dict[str, Any]:
    try:
        return _drafts[name]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Strategy draft not found") from exc


@app.post("/risk/evaluate")
def evaluate_risk(request: RiskRequest) -> dict[str, Any]:
    return _gate.evaluate(_risk_request(request)).to_dict()


@app.get("/risk/status")
def risk_status() -> dict[str, Any]:
    return {
        "mode": "paper",
        "live_keys_locked": True,
        "gate": _gate.status(),
    }


@app.post("/paper/orders")
def submit_paper_order(request: PaperOrderRequest) -> dict[str, Any]:
    risk_request = _risk_request(request)
    execution_request = ExecutionRequest(
        request_id=risk_request.request_id,
        idempotency_key=risk_request.idempotency_key,
        actor_id=risk_request.actor_id,
        connector_id=risk_request.connector_id,
        mode=risk_request.mode,
        symbol=risk_request.symbol,
        side=risk_request.side,
        quantity=risk_request.quantity,
        price=risk_request.price,
        leverage=risk_request.leverage,
        reduce_only=risk_request.reduce_only,
    )
    return _executor.submit(execution_request)


@app.get("/paper/session")
def paper_session() -> dict[str, Any]:
    return {
        "mode": "paper",
        "status": "active",
        "simulated_fills": len(_executor.fills),
        "live_keys_locked": True,
    }

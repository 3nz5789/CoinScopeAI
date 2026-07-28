"""
Shared pytest configuration and fixtures.
"""

import os
import sys

# Ensure project root is on sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

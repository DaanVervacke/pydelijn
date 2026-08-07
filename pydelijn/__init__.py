"""Async client library for the De Lijn (Flemish public transport) open data API."""

from .client import DeLijnClient
from .exceptions import (
    DeLijnAuthError,
    DeLijnConnectionError,
    DeLijnError,
    DeLijnNotFoundError,
    DeLijnResponseError,
)
from .models import Line, Passage, Stop

__version__ = "2.0.1"

__all__ = [
    "DeLijnAuthError",
    "DeLijnClient",
    "DeLijnConnectionError",
    "DeLijnError",
    "DeLijnNotFoundError",
    "DeLijnResponseError",
    "Line",
    "Passage",
    "Stop",
    "__version__",
]

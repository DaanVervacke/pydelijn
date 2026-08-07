"""Exceptions raised by the pydelijn client.

All exceptions carry a human readable message describing what went wrong.
None of them include the request URL or headers, since the subscription
key travels in a header and must never leak into logs or tracebacks.
"""

from __future__ import annotations


class DeLijnError(Exception):
    """Base exception for all pydelijn errors."""


class DeLijnConnectionError(DeLijnError):
    """Raised when the API can't be reached (network error or timeout)."""


class DeLijnAuthError(DeLijnError):
    """Raised on HTTP 401/403: the subscription key is missing or invalid."""


class DeLijnNotFoundError(DeLijnError):
    """Raised on HTTP 404: the requested stop, line, or resource is unknown."""


class DeLijnResponseError(DeLijnError):
    """Raised for any other bad response: unexpected status or invalid JSON."""

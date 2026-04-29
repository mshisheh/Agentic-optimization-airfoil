"""Very small in-memory cache utilities."""

from __future__ import annotations

from typing import Any, Dict

_CACHE: Dict[str, Any] = {}


def get(key: str) -> Any:
    return _CACHE.get(key)


def set_(key: str, value: Any) -> None:
    _CACHE[key] = value

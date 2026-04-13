"""Utility helpers for template projects."""


def clamp(value: float, low: float, high: float) -> float:
    """Clamp a value into [low, high]."""
    return max(low, min(high, value))
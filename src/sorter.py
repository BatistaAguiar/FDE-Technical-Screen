"""
Sorter for FDE Technical Screen.
Implements sort(width, height, length, mass) -> 'STANDARD'|'SPECIAL'|'REJECTED'
"""

from typing import Union


Number = Union[int, float]


def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    """Return destination stack for a package.

    Rules:
    - Bulky: volume >= 1_000_000 cm^3 or any dimension >= 150 cm
    - Heavy: mass >= 20 kg

    Returns one of: 'STANDARD', 'SPECIAL', 'REJECTED'
    """
    try:
        w: float = float(width)
        h: float = float(height)
        l: float = float(length)
        m: float = float(mass)
    except Exception:
        raise TypeError("width, height, length and mass must be numbers")

    if w <= 0 or h <= 0 or l <= 0 or m <= 0:
        raise ValueError("width, height, length and mass must be positive numbers")

    volume: float = w * h * l
    is_bulky: bool = (volume >= 1_000_000) or (w >= 150) or (h >= 150) or (l >= 150)
    is_heavy: bool = m >= 20

    if is_bulky and is_heavy:
        return "REJECTED"

    result = "SPECIAL" if (is_bulky or is_heavy) else "STANDARD"
    return result

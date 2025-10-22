from typing import SupportsFloat, Literal, Callable, Any
import math

BULKY_VOLUME_THRESHOLD_CM3 = 1_000_000.0
BULKY_DIMENSION_THRESHOLD_CM = 150.0
HEAVY_MASS_THRESHOLD_KG = 20.0

Category = Literal["STANDARD", "SPECIAL", "REJECTED"]

def validate_numbers_and_cast(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that validates and casts the first four parameters (width, height, length, mass) to floats.

    The same rules as the previous helper are enforced:
    - bool values are rejected
    - values must be numeric and castable to float
    - values must be finite and > 0
    """
    def wrapper(*f_args: Any, **f_kwargs: Any) -> Any:
        param_names = ("width", "height", "length", "mass")
        args_list = list(f_args)

        for i, name in enumerate(param_names):
            provided_as_pos = i < len(args_list)
            if provided_as_pos:
                val = args_list[i]
            elif name in f_kwargs:
                val = f_kwargs[name]
            else:
                continue

            if isinstance(val, bool):
                raise TypeError(f"{name} must be a number (bool is not allowed)")

            try:
                cast_val = float(val)
            except Exception:
                raise TypeError("width, height, length and mass must be numbers")

            if not math.isfinite(cast_val):
                raise ValueError("width, height, length and mass must be finite numbers")
            if cast_val <= 0.0:
                raise ValueError("width, height, length and mass must be positive numbers")

            if provided_as_pos:
                args_list[i] = cast_val
            else:
                f_kwargs[name] = cast_val

        return func(*args_list, **f_kwargs)

    from functools import wraps

    wrapped = wraps(func)(wrapper)
    return wrapped


@validate_numbers_and_cast
def sort(width: SupportsFloat, height: SupportsFloat, length: SupportsFloat, mass: SupportsFloat) -> Category:
    """
    Classify a package per FDE screening rules.

    Returns: "STANDARD" | "SPECIAL" | "REJECTED"
    """
    bulky_by_dimension = (width >= BULKY_DIMENSION_THRESHOLD_CM
                          or height >= BULKY_DIMENSION_THRESHOLD_CM
                          or length >= BULKY_DIMENSION_THRESHOLD_CM)

    remaining = BULKY_VOLUME_THRESHOLD_CM3
    bulky_by_volume = False
    if not bulky_by_dimension:
        if width != 0 and height != 0:
            remaining /= width
            remaining /= height
            bulky_by_volume = (length >= remaining)
        else:
            bulky_by_volume = False

    is_bulky = bulky_by_dimension or bulky_by_volume
    is_heavy = (mass >= HEAVY_MASS_THRESHOLD_KG)

    if is_bulky and is_heavy:
        return "REJECTED"
    return "SPECIAL" if (is_bulky or is_heavy) else "STANDARD"
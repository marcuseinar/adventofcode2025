"""Helper utilities for Advent of Code solutions."""

import time
from functools import wraps


def timing(func):
    """
    Decorator to measure and print execution time of a function.
    
    Args:
        func: The function to time
    
    Returns:
        Wrapped function that prints execution time
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {(end - start) * 1000:.2f}ms")
        return result
    return wrapper

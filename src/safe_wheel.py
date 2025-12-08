"""Safe wheel simulator function for turning a combination lock wheel."""

from enum import Enum


class Direction(Enum):
    """Enum representing the direction of wheel rotation."""
    CLOCKWISE = 'clockwise'
    COUNTER_CLOCKWISE = 'counter_clockwise'


def safe_wheel(current_position: int, steps: int, direction: Direction, wheel_size: int) -> int:
    """
    Simulate turning a wheel on a safe.
    
    Args:
        current_position: The current position on the wheel (0-indexed).
        steps: The number of steps to turn the wheel.
        direction: The direction of the turn (Direction.CLOCKWISE or Direction.COUNTER_CLOCKWISE).
        wheel_size: The total number of positions on the wheel.
    
    Returns:
        The new position on the wheel after the turn.
    
    Examples:
        >>> safe_wheel(3, 5, Direction.CLOCKWISE, 10)
        8
        >>> safe_wheel(3, 5, Direction.COUNTER_CLOCKWISE, 10)
        8
        
    Note:
        Both examples return 8 because of modular arithmetic:
        - Clockwise: (3 + 5) % 10 = 8
        - Counter-clockwise: (3 - 5) % 10 = -2 % 10 = 8
    """
    if direction == Direction.CLOCKWISE:
        new_position = (current_position + steps) % wheel_size
    elif direction == Direction.COUNTER_CLOCKWISE:
        new_position = (current_position - steps) % wheel_size
    else:
        raise ValueError(f"Invalid direction: {direction}. Must be Direction.CLOCKWISE or Direction.COUNTER_CLOCKWISE.")
    
    return new_position

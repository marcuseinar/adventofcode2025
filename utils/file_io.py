"""File I/O utilities for reading puzzle inputs."""

import os
from pathlib import Path


def read_input(day: int, filename: str = "input.txt") -> str:
    """
    Read the input file for a specific day.
    
    Args:
        day: The day number (1-25)
        filename: Name of the input file (default: "input.txt")
    
    Returns:
        The contents of the input file as a string
    """
    day_dir = Path(__file__).parent.parent / f"day{day:02d}" / "input"
    input_path = day_dir / filename
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    with open(input_path, 'r') as f:
        return f.read()


def read_lines(day: int, filename: str = "input.txt", strip: bool = True) -> list[str]:
    """
    Read the input file and return as a list of lines.
    
    Args:
        day: The day number (1-25)
        filename: Name of the input file (default: "input.txt")
        strip: Whether to strip whitespace from each line (default: True)
    
    Returns:
        List of lines from the input file
    """
    content = read_input(day, filename)
    lines = content.splitlines()
    
    if strip:
        lines = [line.strip() for line in lines]
    
    return lines


def read_ints(day: int, filename: str = "input.txt", separator: str = None) -> list[int]:
    """
    Read the input file and parse as integers.
    
    Args:
        day: The day number (1-25)
        filename: Name of the input file (default: "input.txt")
        separator: String to split on (default: whitespace/newlines)
    
    Returns:
        List of integers from the input file
    """
    content = read_input(day, filename)
    
    if separator:
        return [int(x) for x in content.split(separator) if x.strip()]
    else:
        return [int(x) for x in content.split() if x.strip()]

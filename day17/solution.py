"""Advent of Code 2025 - Day 17"""

import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.helpers import timing


@timing
def part1(input_text: str) -> int:
    """
    Solve part 1 of day 17.
    
    Args:
        input_text: The puzzle input as a string
    
    Returns:
        The solution to part 1
    """
    # TODO: Implement solution for day 17 part 1
    raise NotImplementedError("Solution for Day 17 Part 1 has not been implemented yet.")


@timing
def part2(input_text: str) -> int:
    """
    Solve part 2 of day 17.
    
    Args:
        input_text: The puzzle input as a string
    
    Returns:
        The solution to part 2
    """
    # TODO: Implement solution for day 17 part 2
    raise NotImplementedError("Solution for Day 17 Part 2 has not been implemented yet.")


def main():
    """Main entry point for running this day's solutions."""
    # Read input file
    day_dir = Path(__file__).parent
    input_file = day_dir / "input" / "input.txt"
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        return 1
    
    with open(input_file) as f:
        input_text = f.read()
    
    # Determine which part to run
    part = None
    if len(sys.argv) > 1:
        part = sys.argv[1]
    
    # Run the requested part(s)
    exit_code = 0
    
    if part is None or part == "1":
        try:
            result = part1(input_text)
            print(f"Day 17 Part 1 Solution: {result}")
        except NotImplementedError as e:
            print(f"Day 17 Part 1: {e}")
            exit_code = 1
    
    if part is None or part == "2":
        try:
            result = part2(input_text)
            print(f"Day 17 Part 2 Solution: {result}")
        except NotImplementedError as e:
            print(f"Day 17 Part 2: {e}")
            exit_code = 1
    
    return exit_code


if __name__ == "__main__":
    exit(main())

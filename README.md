# Advent of Code 2025

Solutions for Advent of Code 2025

## Project Structure

```
adventofcode2025/
├── day01/               # Day 1 solutions
│   ├── __init__.py     # Package marker
│   ├── solution.py     # Both parts in one file
│   └── input/          # Input files for day 1
│       └── input.txt
├── day02/               # Day 2 solutions
│   └── ...
├── ...                  # Days 3-25 follow the same structure
├── utils/               # Reusable utility functions
│   ├── __init__.py
│   ├── file_io.py      # File reading utilities
│   └── helpers.py      # Helper functions (timing, etc.)
├── run.py               # Main runner script
└── venv/                # Virtual environment
```

## Setup

1. **Create and activate virtual environment** (already created):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies** (if any are added later):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Solutions

The `run.py` script is the main entry point for running solutions:

```bash
# Run current day's solution (both parts)
python run.py

# Run a specific day (both parts)
python run.py --day 5

# Run a specific day and part
python run.py --day 5 --part 1

# Run all days (both parts)
python run.py --all
```

### Running Individual Solutions

You can also run individual solution files directly:

```bash
# From the project root (runs both parts)
python day01/solution.py

# Or from within a day directory (runs both parts)
cd day01
python solution.py

# Run a specific part
python solution.py 1  # Run only part 1
python solution.py 2  # Run only part 2
```

## Adding Your Solution

1. Navigate to the appropriate day folder (e.g., `day01/`)
2. Edit `solution.py`
3. Replace the `NotImplementedError` in `part1()` and/or `part2()` functions
4. Add your input data to `input/input.txt`
5. Run your solution using `python run.py --day X` or `python dayXX/solution.py`

### Example Solution Structure

```python
"""Advent of Code 2025 - Day 1"""

from utils.helpers import timing


@timing
def part1(input_text: str) -> int:
    """
    Solve part 1 of day 1.
    
    Args:
        input_text: The puzzle input as a string
    
    Returns:
        The solution to part 1
    """
    lines = input_text.strip().split('\n')
    
    # Your solution logic here
    result = 0
    
    return result


@timing
def part2(input_text: str) -> int:
    """
    Solve part 2 of day 1.
    
    Args:
        input_text: The puzzle input as a string
    
    Returns:
        The solution to part 2
    """
    lines = input_text.strip().split('\n')
    
    # Your solution logic here
    result = 0
    
    return result


def main():
    """Main entry point for running this day's solutions."""
    import sys
    from pathlib import Path
    
    # Read input file
    day_dir = Path(__file__).parent
    input_file = day_dir / "input" / "input.txt"
    
    with open(input_file) as f:
        input_text = f.read()
    
    # Determine which part to run
    part = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Run the requested part(s)
    if part is None or part == "1":
        try:
            result = part1(input_text)
            print(f"Day 1 Part 1 Solution: {result}")
        except NotImplementedError as e:
            print(f"Day 1 Part 1: {e}")
    
    if part is None or part == "2":
        try:
            result = part2(input_text)
            print(f"Day 1 Part 2 Solution: {result}")
        except NotImplementedError as e:
            print(f"Day 1 Part 2: {e}")


if __name__ == "__main__":
    main()
```

## Utility Functions

The `utils` module provides helpful functions and decorators:

### Helpers (`utils.helpers`)

- **`@timing`** - Decorator to measure and print execution time of a function. This decorator wraps your solve functions and automatically prints how long they took to run in milliseconds.

### File I/O (`utils.file_io`)

While the new structure passes input text directly to solve functions, these utilities are still available if needed:

- `read_input(day, filename='input.txt')` - Read entire input file as string
- `read_lines(day, filename='input.txt', strip=True)` - Read input as list of lines
- `read_ints(day, filename='input.txt', separator=None)` - Read input as list of integers

## Notes

- Each day has a single `solution.py` file containing both `part1()` and `part2()` functions
- All days have been pre-created with placeholder solutions that raise `NotImplementedError`
- When a solution is not implemented, running it will display: "Solution for Day X Part Y has not been implemented yet."
- Input files should be placed in the `dayXX/input/` directory
- The virtual environment (`venv/`) is included in `.gitignore`
- Solutions are organized as a Python package structure for clean imports

## License

See LICENSE file for details.

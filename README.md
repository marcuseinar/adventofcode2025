# Advent of Code 2025

Solutions for Advent of Code 2025

## Project Structure

```
adventofcode2025/
├── day01/               # Day 1 solutions
│   ├── part1.py        # Part 1 solution
│   ├── part2.py        # Part 2 solution
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
# From the project root
python day01/part1.py

# Or from within a day directory
cd day01
python part1.py
```

## Adding Your Solution

1. Navigate to the appropriate day folder (e.g., `day01/`)
2. Edit `part1.py` or `part2.py`
3. Replace the `NotImplementedError` with your solution logic
4. Add your input data to `input/input.txt`
5. Run your solution using `python run.py --day X --part Y`

### Example Solution Structure

```python
"""Advent of Code 2025 - Day 1 Part 1"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import read_input, read_lines, timing


@timing
def solve(day: int) -> int:
    """Solve part 1 of day 1."""
    lines = read_lines(day)
    
    # Your solution logic here
    result = 0
    
    return result


def main():
    day = 1
    try:
        result = solve(day)
        print(f"Day {day} Part 1 Solution: {result}")
    except NotImplementedError as e:
        print(f"Day {day} Part 1: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
```

## Utility Functions

The `utils` module provides helpful functions for reading input and timing solutions:

### File I/O (`utils.file_io`)

- `read_input(day, filename='input.txt')` - Read entire input file as string
- `read_lines(day, filename='input.txt', strip=True)` - Read input as list of lines
- `read_ints(day, filename='input.txt', separator=None)` - Read input as list of integers

### Helpers (`utils.helpers`)

- `@timing` - Decorator to measure and print execution time

## Notes

- All days have been pre-created with placeholder solutions
- When a solution is not implemented, running it will display: "Solution for Day X Part Y has not been implemented yet."
- Input files should be placed in the `dayXX/input/` directory
- The virtual environment (`venv/`) is included in `.gitignore`

## License

See LICENSE file for details.

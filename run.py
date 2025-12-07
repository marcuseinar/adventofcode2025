#!/usr/bin/env python3
"""
Advent of Code 2025 Runner Script

This script runs solutions for specified days of Advent of Code 2025.
By default, it runs today's solution. You can specify different days or parts.

Usage:
    python run.py                  # Run current day (both parts)
    python run.py --day 5          # Run day 5 (both parts)
    python run.py --day 5 --part 1 # Run day 5 part 1 only
    python run.py --all            # Run all days (both parts)
"""

import argparse
import sys
import importlib
from datetime import datetime
from pathlib import Path


def get_current_day() -> int:
    """
    Get the current day in December (for Advent of Code).
    Returns 1 if before December or after day 25.
    
    Returns:
        Current day number (1-25)
    """
    now = datetime.now()
    
    # Check if it's December
    if now.month != 12:
        return 1
    
    # Check if it's day 1-25
    day = now.day
    if day > 25:
        return 25
    
    return day


def run_solution(day: int, part: int = None) -> int:
    """
    Run a specific day and optionally a specific part.
    
    Args:
        day: The day number (1-25)
        part: The part number (1 or 2), or None for both parts
    
    Returns:
        Exit code (0 for success, 1 for not implemented/error)
    """
    day_padded = f"{day:02d}"
    day_module = f"day{day_padded}"
    
    # Check if solution file exists
    solution_file = Path(__file__).parent / day_module / "solution.py"
    if not solution_file.exists():
        print(f"Error: Solution file not found: {solution_file}")
        return 1
    
    # Read input file
    input_file = Path(__file__).parent / day_module / "input" / "input.txt"
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        return 1
    
    with open(input_file) as f:
        input_text = f.read()
    
    # Import the solution module dynamically
    try:
        module = importlib.import_module(day_module + ".solution")
    except Exception as e:
        print(f"Error importing solution module: {e}")
        return 1
    
    # Determine which parts to run
    parts_to_run = [part] if part else [1, 2]
    
    exit_code = 0
    for part_num in parts_to_run:
        print(f"\n{'=' * 60}")
        print(f"Running Day {day} Part {part_num}")
        print(f"{'=' * 60}")
        
        try:
            # Get the part function
            part_func = getattr(module, f"part{part_num}")
            
            # Run the solution
            result = part_func(input_text)
            print(f"Day {day} Part {part_num} Solution: {result}")
            
        except NotImplementedError as e:
            print(f"Day {day} Part {part_num}: {e}")
            exit_code = 1
        except AttributeError:
            print(f"Error: part{part_num} function not found in {day_module}.solution")
            exit_code = 1
        except Exception as e:
            print(f"Error running solution: {e}")
            exit_code = 1
    
    return exit_code


def main():
    """Main entry point for the runner script."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2025 solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        '--day', '-d',
        type=int,
        choices=range(1, 26),
        metavar='DAY',
        help='Day to run (1-25). Defaults to current day.'
    )
    
    parser.add_argument(
        '--part', '-p',
        type=int,
        choices=[1, 2],
        metavar='PART',
        help='Part to run (1 or 2). If not specified, runs both parts.'
    )
    
    parser.add_argument(
        '--all', '-a',
        action='store_true',
        help='Run all days (both parts)'
    )
    
    args = parser.parse_args()
    
    # Determine which days to run
    if args.all:
        days_to_run = list(range(1, 26))
    elif args.day:
        days_to_run = [args.day]
    else:
        days_to_run = [get_current_day()]
    
    # Print summary
    print("\nAdvent of Code 2025 - Solution Runner")
    print("=" * 60)
    if args.all:
        print("Running: All days")
    else:
        print(f"Running: Day {days_to_run[0]}")
    
    if args.part:
        print(f"Parts: Part {args.part}")
    else:
        print("Parts: Both parts")
    print()
    
    # Run solutions
    exit_codes = []
    for day in days_to_run:
        exit_code = run_solution(day, args.part)
        exit_codes.append(exit_code)
    
    # Summary
    print(f"\n{'=' * 60}")
    print("Summary")
    print(f"{'=' * 60}")
    
    total = len(exit_codes)
    successful = sum(1 for code in exit_codes if code == 0)
    not_implemented = total - successful
    
    print(f"Total days run: {total}")
    print(f"Successful: {successful}")
    print(f"Not implemented: {not_implemented}")
    
    # Return 0 if all succeeded, 1 otherwise
    return 0 if successful == total else 1


if __name__ == "__main__":
    sys.exit(main())

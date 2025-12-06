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
import subprocess
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


def run_solution(day: int, part: int) -> int:
    """
    Run a specific day and part solution.
    
    Args:
        day: The day number (1-25)
        part: The part number (1 or 2)
    
    Returns:
        Exit code from the solution script
    """
    day_padded = f"{day:02d}"
    solution_dir = Path(__file__).parent / f"day{day_padded}"
    solution_file = solution_dir / f"part{part}.py"
    
    if not solution_file.exists():
        print(f"Error: Solution file not found: {solution_file}")
        return 1
    
    print(f"\n{'=' * 60}")
    print(f"Running Day {day} Part {part}")
    print(f"{'=' * 60}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(solution_file)],
            cwd=solution_dir,
            capture_output=False,
            text=True
        )
        return result.returncode
    except Exception as e:
        print(f"Error running solution: {e}")
        return 1


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
    
    # Determine which parts to run
    parts_to_run = [args.part] if args.part else [1, 2]
    
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
        for part in parts_to_run:
            exit_code = run_solution(day, part)
            exit_codes.append(exit_code)
    
    # Summary
    print(f"\n{'=' * 60}")
    print("Summary")
    print(f"{'=' * 60}")
    
    total = len(exit_codes)
    successful = sum(1 for code in exit_codes if code == 0)
    not_implemented = sum(1 for code in exit_codes if code == 1)
    
    print(f"Total solutions run: {total}")
    print(f"Successful: {successful}")
    print(f"Not implemented: {not_implemented}")
    print(f"Errors: {total - successful - not_implemented}")
    
    # Return 0 if all solutions either succeeded or are not implemented
    # Return 1 if there were actual errors
    if total - successful - not_implemented > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

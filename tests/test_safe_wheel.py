"""Tests for the safe_wheel function."""

import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from safe_wheel import safe_wheel


class TestSafeWheel(unittest.TestCase):
    """Test cases for the safe_wheel function."""
    
    def test_clockwise_basic(self):
        """Test basic clockwise rotation."""
        assert safe_wheel(3, 5, 'clockwise', 10) == 8
    
    def test_counter_clockwise_basic(self):
        """Test basic counter-clockwise rotation."""
        assert safe_wheel(3, 5, 'counter_clockwise', 10) == 8
    
    def test_clockwise_wraparound(self):
        """Test clockwise rotation that wraps around."""
        assert safe_wheel(8, 5, 'clockwise', 10) == 3
    
    def test_counter_clockwise_wraparound(self):
        """Test counter-clockwise rotation that wraps around."""
        assert safe_wheel(2, 5, 'counter_clockwise', 10) == 7
    
    def test_zero_steps(self):
        """Test that zero steps returns the same position."""
        assert safe_wheel(5, 0, 'clockwise', 10) == 5
        assert safe_wheel(5, 0, 'counter_clockwise', 10) == 5
    
    def test_full_rotation_clockwise(self):
        """Test a full rotation clockwise returns to start."""
        assert safe_wheel(5, 10, 'clockwise', 10) == 5
    
    def test_full_rotation_counter_clockwise(self):
        """Test a full rotation counter-clockwise returns to start."""
        assert safe_wheel(5, 10, 'counter_clockwise', 10) == 5
    
    def test_steps_larger_than_wheel_size(self):
        """Test that steps larger than wheel_size work correctly."""
        # 15 steps on a 10-position wheel = 1.5 rotations = position 5
        assert safe_wheel(0, 15, 'clockwise', 10) == 5
        assert safe_wheel(0, 15, 'counter_clockwise', 10) == 5
    
    def test_multiple_rotations(self):
        """Test multiple full rotations."""
        assert safe_wheel(3, 23, 'clockwise', 10) == 6  # 3 + 23 = 26, 26 % 10 = 6
        assert safe_wheel(7, 27, 'counter_clockwise', 10) == 0  # 7 - 27 = -20, -20 % 10 = 0
    
    def test_different_wheel_sizes(self):
        """Test with different wheel sizes."""
        assert safe_wheel(0, 1, 'clockwise', 12) == 1
        assert safe_wheel(0, 1, 'clockwise', 20) == 1
        assert safe_wheel(0, 1, 'clockwise', 60) == 1
    
    def test_edge_positions(self):
        """Test starting at edge positions."""
        assert safe_wheel(0, 1, 'clockwise', 10) == 1
        assert safe_wheel(9, 1, 'clockwise', 10) == 0
        assert safe_wheel(0, 1, 'counter_clockwise', 10) == 9
        assert safe_wheel(9, 1, 'counter_clockwise', 10) == 8
    
    def test_invalid_direction(self):
        """Test that invalid direction raises ValueError."""
        with self.assertRaises(ValueError):
            safe_wheel(0, 1, 'invalid', 10)
        with self.assertRaises(ValueError):
            safe_wheel(0, 1, 'left', 10)


if __name__ == '__main__':
    unittest.main()

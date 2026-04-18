# test_amberdata.py
"""
Tests for Amberdata module.
"""

import unittest
from amberdata import Amberdata

class TestAmberdata(unittest.TestCase):
    """Test cases for Amberdata class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Amberdata()
        self.assertIsInstance(instance, Amberdata)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Amberdata()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

__all__ = ["get_data"]
__author__ = """whege"""
__date__ = "9/30/2022"
__doc__ = """Test for get_data"""

from datetime import date
import unittest

from src.data.get_data import get_data


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        get_data(date(2022, 1, 1), date(2022, 3, 1))


if __name__ == '__main__':
    unittest.main()

import unittest

from src.data.load_data import load_from_disk


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = load_from_disk()
        self.assertNotEqual(data, [])


if __name__ == '__main__':
    unittest.main()

import unittest
from process import heightValidator

class TestProcess(unittest.TestCase):
    def test_height_validator(self):
        self.assertTrue(heightValidator("169cm"))

if __name__ == '__main__':
    unittest.main()
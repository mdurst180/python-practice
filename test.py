import unittest

from warmups import diff21

class TestSum(unittest.TestCase):

    def test_diff21(self):
        self.assertEqual(diff21(21), 0, "Should be 0")

    def test_diff21_lessthan21(self):
        self.assertEqual(diff21(20), 1, "Should be 1")

    def test_diff21_greaterthan21(self):
        self.assertEqual(diff21(22), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
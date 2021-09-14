import unittest
import basics

class TestBasics(unittest.TestCase):

    def test_diff21(self):
        self.assertEqual(basics.diff21(21), 0, "Should be 0")

    def test_diff21_lessthan21(self):
        self.assertEqual(basics.diff21(20), 1, "Should be 1")

    def test_diff21_greaterthan21(self):
        self.assertEqual(basics.diff21(22), 2, "Should be 2")

    def test_near_hundred_95(self):
        self.assertEqual(basics.near_hundred(95), True, "Should be True")

    def test_near_hundred_89(self):
        self.assertEqual(basics.near_hundred(89), False, "Should be False")

if __name__ == '__main__':
    unittest.main()
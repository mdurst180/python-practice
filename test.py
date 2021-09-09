import unittest

from warmups import diff21

class TestSum(unittest.TestCase):

    def test_diff21(self):
        self.assertEqual(diff21(21), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()
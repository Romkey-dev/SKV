import unittest

from app import add


class AdditionTests(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 2), 0)

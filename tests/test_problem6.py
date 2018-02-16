import unittest
from euler.problem6 import Problem6


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(25164150, Problem6(range(1, 101)).square_difference())

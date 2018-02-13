import unittest
from euler.problem1 import Problem1


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(233168, Problem1(1000).multiples())

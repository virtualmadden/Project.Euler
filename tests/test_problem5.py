import unittest
from euler.problem5 import Problem5


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(232792560, Problem5(range(1, 21)).smallest_multiples())

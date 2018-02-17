import unittest
from euler.problem7 import Problem7


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(104743, Problem7(10001).primes())

import unittest
from euler.problem3 import Problem3


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(6857, Problem3(600851475143).largest_prime())

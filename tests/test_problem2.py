import unittest
from euler.problem2 import Problem2


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(4613732, Problem2(4000000).fibonacci())

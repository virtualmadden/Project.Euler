import unittest
from euler.problem4 import Problem4


class TestEngine(unittest.TestCase):
    def test_shouldReturnSolution(self):
        self.assertEqual(906609, Problem4(3).fibonacci())

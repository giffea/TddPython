import unittest

from bowling.BowlingScoreCalculator import *


class BowlingScoreCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = BowlingScoreCalculator()
        pass

    def tearDown(self):
        pass

    def testIntputBallNumber(self):
        # Given the pinfall of 21 balls
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)

        # Then it is a valid input
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

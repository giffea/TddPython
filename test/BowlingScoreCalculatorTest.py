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

    def testInputPinfallLessThan0(self):
        # Given the pinfall which < 0
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)

        # Then it is not a valid input
        self.assertFalse(result)

    def testInputPinfallMoreThan10(self):
        # Given the pinfall which > 10
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)

        # Then it is not a valid input
        self.assertFalse(result)

    def testInputSumOfPinfallOfOneFrameNotGreatThan10(self):
        # Given the pinfall of one frame <= 10
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)

        # Then it is a valid input
        self.assertTrue(result)

    def testInputSumOfPinfallOfOneFrameGreatThan10(self):
        # Given the pinfall of one frame > 10
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)
        
        # Then it is not a valid input
        self.assertFalse(result)

    def testInput1StrikeOnFrame10(self):
        # Given the pinfall of ball 1 and ball 2 of frame 10 are all strike
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 0]

        # When check if the inputs are valid numbers
        result = self.calculator.checkInputs(inputs)

        # Then it is a valid input
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)

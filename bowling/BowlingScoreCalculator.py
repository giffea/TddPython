#! /usr/env python3


class BowlingScoreCalculator:
    kMaxBallNum = 21

    def __init__(self):
        pass

    def checkInputs(self, inputs):
        if len(inputs) != self.kMaxBallNum:
            return False

        return True

#! /usr/env python3


class BowlingScoreCalculator:
    kMaxBallNum = 21
    kMinPinfall = 0

    def __init__(self):
        pass

    def checkInputs(self, inputs):
        if len(inputs) != self.kMaxBallNum:
            return False

        for iBall in range(self.kMaxBallNum):
            pinfall = inputs[iBall]
            if pinfall < self.kMinPinfall:
                return False

        return True

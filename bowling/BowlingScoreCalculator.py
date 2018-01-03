#! /usr/env python3


class BowlingScoreCalculator:
    kMaxBallNum = 21
    kMinPinfall = 0
    kMaxPinfall = 10
    kTotalFrame = 10

    def __init__(self):
        pass

    def checkInputs(self, inputs):
        if len(inputs) != self.kMaxBallNum:
            return False

        for iBall in range(self.kMaxBallNum):
            pinfall = inputs[iBall]
            if pinfall < self.kMinPinfall:
                return False
            elif pinfall > self.kMaxPinfall:
                return False

        for iFrame in range(self.kTotalFrame):
            pinfall1 = inputs[iFrame * 2]
            pinfall2 = inputs[iFrame * 2 + 1]
            if pinfall1 + pinfall2 > self.kMaxPinfall:
                if iFrame == self.kTotalFrame - 1:
                    if pinfall1 == 10:
                        return True
                return False

        return True

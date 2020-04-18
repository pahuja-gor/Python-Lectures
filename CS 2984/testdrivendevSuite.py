import unittest
import testdrivendev

class TestAnnoyingNumberGame(unittest.TestCase):

    def testComputerNumberGreaterThan0(self):
        assert testdrivendev.computerGuess() > 0, "Computer Number was NOT greater than 0"

    def testComputerNumberLessThan101(self):
        assert testdrivendev.computerGuess() < 101, "Computer Number is too large!"

    def testUserNumberGreaterThan0(self):
        assert testdrivendev.userGuess() > 0, "user number was too small"

    def testUserNumberLessThan101(self):
        assert testdrivendev.userGuess() < 101, "user number was too large"

    def testGuessTooLow(self):
        assert testdrivendev.provideFeedback(50, 49) == "too low", "number is too high"

    def testGuessTooHigh(self):
        assert testdrivendev.provideFeedback(49, 50) == "too high", "number is too low"

    def testGuessCorrectly(self):
        assert testdrivendev.provideFeedback(50, 50) == "user's guess was correct", "user's guess was incorrect"

if __name__ == '__main__':
    unittest.main()
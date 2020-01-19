# 2020-1-19 Mikko Mustonen
import unittest
import os

from fibonacci import Fibonaccinator


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonaccinator = Fibonaccinator()

    def test_output(self):
        testList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.fibonaccinator.saveToFile(testList)

        f = open(os.path.dirname(os.path.realpath(
            __file__)) + "/fibonacci.txt", "r")
        readList = f.read()
        f.close()

        self.assertTrue(str(testList) == readList)

    def test_input(self):
        self.assertEqual(self.fibonaccinator.inputValidation(
            '', ''), {"startingNumber": 0, "seriesLength": 10})
        self.assertEqual(self.fibonaccinator.inputValidation(
            '3', '13'), {"startingNumber": 3, "seriesLength": 13})
        self.assertEqual(self.fibonaccinator.inputValidation(
            '0', '0'), {"startingNumber": 0, "seriesLength": 0})
        self.assertFalse(self.fibonaccinator.inputValidation('-5', '-5'))
        self.assertFalse(self.fibonaccinator.inputValidation('g', 'g'))
        self.assertFalse(self.fibonaccinator.inputValidation('&', '@'))

    def test_fibonacci(self):
        self.assertEqual(self.fibonaccinator.fibonacciWithStartAndLength(
            {"startingNumber": 0, "seriesLength": 10}), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(self.fibonaccinator.fibonacciWithStartAndLength(
            {"startingNumber": 1, "seriesLength": 10}), [2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(self.fibonaccinator.fibonacciWithStartAndLength(
            {"startingNumber": 6, "seriesLength": 10}), [8, 13, 21, 34, 55, 89, 144, 233, 377, 610])


if __name__ == '__main__':
    unittest.main()

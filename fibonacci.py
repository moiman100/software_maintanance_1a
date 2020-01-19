# 2020-1-19 Mikko Mustonen
import os
import sys


class Fibonaccinator:
    def fibonacciWithStartAndLength(self, numbers):
        previous = 0
        current = 1
        fibonacciList = [previous, current]
        targetIndex = 0

        while True:
            # Phase 1
            if numbers["startingNumber"] < current and targetIndex == 0:
                targetIndex = len(fibonacciList) - 1
            # Phase 2
            if (len(fibonacciList) - targetIndex) >= 10 and targetIndex != 0:
                break
            # Calculating Fibonacci
            current = current + previous
            previous = current - previous
            fibonacciList.append(current)

        return fibonacciList[targetIndex:targetIndex + numbers["seriesLength"]]

    def saveToFile(self, fibonacciList):
        f = open(os.path.dirname(os.path.realpath(
            __file__)) + "/fibonacci.txt", "w")
        f.write(str(fibonacciList))
        f.close()

    def inputValidation(self, startingNumber, seriesLength):
        try:
            if len(startingNumber) == 0:
                startingNumber = 0

            if len(seriesLength) == 0:
                seriesLength = 10

            if int(seriesLength) < 0 or int(startingNumber) < 0:
                print("Can't be negative.")
                return False

        except ValueError:
            print("Invalid value")
            return False

        return {"startingNumber": int(startingNumber), "seriesLength": int(seriesLength)}


def main():

    fibonaccinator = Fibonaccinator()

    validatedInput = False

    while not validatedInput:
        startingNumber = input("Starting number: ")
        seriesLength = input("Series length: ")
        validatedInput = fibonaccinator.inputValidation(startingNumber, seriesLength)

    fibonaccinator.saveToFile(
        fibonaccinator.fibonacciWithStartAndLength(validatedInput))


if __name__ == "__main__":
    main()

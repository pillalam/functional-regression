# Program that implements a simple calculator
import sys


class Calculator:

    def add(self, x, y):

        return x + y

    def subtract(self, x, y):

        return x - y

    def multiply(self, x, y):

        return x * y

    def divide(self, x, y):

        return x / y

result1 = Calculator().add(int(sys.argv[1]), int(sys.argv[2]))
result2 = Calculator().multiply(int(sys.argv[1]), int(sys.argv[2]))
print "Sum:" + str(result1)
print "Product:" + str(result2)

"""
ECE241 Fall 2025 - Homework1 Question2
Andrew Wakefield
"""
import math


class Question2:
    @staticmethod
    def solveMonomial(a, b, c):
        """Solves the monomial for x in the form ax - 2b = c

        Args:
            a: user input
            b: user input
            c: user input

        Returns:
            int: x
        """

        return (2*b + c) / a # solution to x
    
    @staticmethod
    def solvePolynomial(a, b, c):
        """Solves the monomial for x in the form sqrt(ax - 2b) = c

        Args:
            a: user input
            b: user input
            c: user input

        Returns:
            int: x
        """

        return (c**2 - 2*b) / a # solution to x

    @staticmethod
    def autograder():
        monomial_result = "36.14705882352941"
        polynomial_result = "869.7352941176471"

        # Do NOT change the code below!
        return {
            "monomial": monomial_result,
            "polynomial": polynomial_result
        }


if __name__ == "__main__":
    a = int(input("Please input the value for a: "))
    b = int(input("Please input the value for b: "))
    c = int(input("Please input the value for c: "))
    print("Monomial:", Question2.solveMonomial(a, b, c))
    print("Polynomial:", Question2.solvePolynomial(a, b, c))
from abc import ABC


class Model(ABC):
    """Abstract base class"""
    pass


class CollatzCalculation(Model):
    """
    An interator class for calculation the Collatz Conjecture.
    Theory goes like this:
        If the number is even, divide by two.
        If the number is odd, divide, multiply by three and add one.

    Find a number that doesn't end in 4-2-1 loop.
    For more information, see here: https://en.wikipedia.org/wiki/Collatz_conjecture
    """

    def __init__(self, num: int):
        if num < 0:
            raise ValueError("You should input a positive number.")
        self.curr = num

    def __iter__(self):
        """
        :return: iteratior object containing numbers of Collatz Conjecture.
        """
        return self

    def __next__(self) -> int:
        """
        This works assuming that the theory of every positive number always ends in the loop of 4-2-1 numbers.
        :return: integer number
        """
        if self.curr != 1:
            if self.curr % 2 == 0:
                self.curr = self.curr // 2

            else:
                self.curr = 3 * self.curr + 1

            return self.curr

        else:
            raise StopIteration

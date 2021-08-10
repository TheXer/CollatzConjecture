import matplotlib.pyplot as plt
from typing import List

"""
A practice code for trying out the Model-View-Controller design pattern.
"""


class CollatzCalculation:
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


class GraphView:
    """
    View for the 'model' (CollatzCalculation class), shows graphs with the numbers.
    """
    def __init__(self):
        self.plt = plt

    @classmethod
    def lentgh(cls, numbers: List[int]) -> int:
        return len(numbers)

    def plot(self, numbers: List[int]) -> plt:
        self.plt.plot(numbers)

        for index, number in enumerate(numbers):
            self.plt.text(index, number, str(number))

        self.plt.grid()
        self.plt.show()


class Controller:
    """
    Basic contorller class.
    """
    def __init__(self, calculation: CollatzCalculation, view: GraphView):
        self.calculation = calculation
        self.view = view

    def get_view(self) -> plt:
        self.view.plot(list(self.calculation))

    def get_lentgh(self) -> int:
        return self.view.lentgh(list(self.calculation))


if __name__ == '__main__':
    c = Controller(CollatzCalculation(87314), GraphView())
    print(c.get_lentgh())

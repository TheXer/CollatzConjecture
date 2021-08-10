from typing import List
import matplotlib.pyplot as plt
from abc import ABC


class View(ABC):
    """Abstract base class"""
    pass


class GraphView(View):
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

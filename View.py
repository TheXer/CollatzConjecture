from typing import List
import matplotlib.pyplot as plt


class GraphView:
    """
    View for the 'model' (CollatzCalculation class), shows graphs with the numbers.
    """

    def __init__(self):
        self.plt = plt

    def plot(self, numbers: List[int]):
        self.plt.plot(numbers)

        for index, number in enumerate(numbers):
            self.plt.text(index, number, str(number))

        self.plt.grid()
        self.plt.show()

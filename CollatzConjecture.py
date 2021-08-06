from typing import List
import matplotlib.pyplot as plt


class CollatzConjecture:
    """
    Inspired by a great Vertasium vid about it.
    Two simple rules:
        - If the number is even, divide by two
        - If the number is odd, multiply by three and add one
    Find a positive number that doesn't end in the loop 4 - 2 - 1
    """

    def __init__(self):
        self.numbers: List[int] = []

    def __len__(self):
        return len(self.numbers)

    def conjecture(self, num: int) -> List[int]:
        """
        For calculating the sequence. Returns a list of integers. Loop breaks when the integer equals to 1.
        :param num: int
        :return: List[int]
        """
        self.numbers.append(num)
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (3 * num) + 1
            self.numbers.append(num)
        return self.numbers

    def plot(self) -> plt:
        """
        Show a graph out of sequence
        """
        plt.plot(self.numbers)
        for index, number in enumerate(self.numbers):
            plt.text(index, number, str(number))
        plt.grid()
        plt.show()

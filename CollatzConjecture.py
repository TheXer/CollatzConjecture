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

    def recursive_collatz(self, num: int) -> int:
        """
        Counting the Collatz Conjecture through recursion, it isn't the fastest snippet of code, you can probably find
        better codes out there if your main objective is speed. This is just for visualization and training purposes.
        """
        self.numbers.append(num)

        if num < 0:
            raise ValueError("Use non-negative numbers!")

        elif num == 1:
            return 1

        elif num % 2 == 0:
            result = num / 2
            self.recursive_collatz(int(result))

        else:
            result = 3 * num + 1
            self.recursive_collatz(int(result))

    def plot(self) -> plt:
        plt.plot(self.numbers)
        for index, number in enumerate(self.numbers):
            plt.text(index, number, str(number))
        plt.grid()
        plt.show()


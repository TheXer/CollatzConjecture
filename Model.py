from database.wrapper import MySQLWrapper


class CollatzCalculation:
    """
    An interator class for calculation the Collatz Conjecture.
    Theory goes like this:
        If the number is even, divide by two.
        If the number is odd, divide, multiply by three and add one.

    Find a number that doesn't end in 4-2-1 loop.
    For more information, see here: https://en.wikipedia.org/wiki/Collatz_conjecture
    """

    def __init__(self, num: int = 20):
        if num < 0:
            raise ValueError("You should input a positive number.")
        self.curr = num

    def __repr__(self):
        return f"First number: {self.curr}, Output: {list(self)}"

    def __iter__(self):
        """
        :return: iterator object containing numbers of Collatz Conjecture.
        """
        return self

    def __next__(self) -> int:
        if self.curr == 1:
            raise StopIteration

        with MySQLWrapper() as db:
            num = db.query(query="SELECT Number FROM Numbers WHERE Number = %s", val=(self.curr,))

            if num:
                self.curr = db.query(query="SELECT `Result` FROM `Numbers` WHERE `Number` = %s", val=(self.curr,))
                self.curr = self.curr[0]

            else:
                num = self.curr
                if self.curr % 2 == 0:
                    self.curr = self.curr // 2

                else:
                    self.curr = 3 * self.curr + 1

                db.execute(query="INSERT INTO `Numbers`(`Number`, `Result`) VALUES (%s, %s)", val=(num, self.curr),
                           commit=True)

        return self.curr

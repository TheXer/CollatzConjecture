from Controller import ControllerCollatz
from View import GraphView
from Model import CollatzCalculation

"""
The script to run. I was trying to look more into the Model View Controller design pattern and tried to practice with 
Collatz Conjecture. 
"""

if __name__ == '__main__':
    c = ControllerCollatz(CollatzCalculation(91), GraphView())
    c.get_view()
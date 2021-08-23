from abc import ABC, abstractmethod

from View import GraphView
from Model import CollatzCalculation


class ControllerCollatz:
    def __init__(self, calculation: CollatzCalculation, view: GraphView):
        self.calculation = calculation
        self.view = view

    def get_view(self):
        self.view.plot(list(self.calculation))
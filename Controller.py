from abc import ABC, abstractmethod

from View import GraphView
from Model import CollatzCalculation


class Controller(ABC):
    """Abstract base class"""

    @abstractmethod
    def get_view(self):
        pass


class ControllerCollatz(Controller):
    def __init__(self, calculation: CollatzCalculation, view: GraphView):
        self.calculation = calculation
        self.view = view

    def get_view(self):
        self.view.plot(list(self.calculation))

    def get_lentgh(self) -> int:
        return self.view.lentgh(list(self.calculation))

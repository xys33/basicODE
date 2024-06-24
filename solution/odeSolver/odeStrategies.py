from abc import ABC, abstractmethod
class ode_strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: list):
        pass

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ode_liniear(ode_strategy):
    """
    The Euler's method - 1st order RK
    """
    def do_algorithm(self, data: list) -> list:
        return sorted(data)

class ode_trapezoidal(ode_strategy):
    """
    2nd order RK
    """
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))
    
class ode_rk4(ode_strategy):
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))
    
class ode_rk45(ode_strategy):
    def do_algorithm(self, data: list) -> list:
        return reversed(sorted(data))
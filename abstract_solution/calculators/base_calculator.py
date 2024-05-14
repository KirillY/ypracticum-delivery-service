from abc import ABC, abstractmethod


class DeliveryCostCalculator(ABC):
    @abstractmethod
    def calculate_cost(
        self,
        delivery_data,
        cost_config,
    ):
        pass

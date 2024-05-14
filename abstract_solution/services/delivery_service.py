class DeliveryService:
    def __init__(
        self,
        cost_calculator,
        cost_config,
    ):
        self.cost_calculator = cost_calculator
        self.cost_config = cost_config

    def calculate_delivery_cost(
        self,
        delivery_data,
    ):
        if delivery_data.is_fragile and delivery_data.distance > 30:
            raise ValueError("Хрупкие грузы нельзя возить на расстояние более 30 км")
        return self.cost_calculator.calculate_cost(delivery_data, self.cost_config)

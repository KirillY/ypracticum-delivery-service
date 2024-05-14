from .base_calculator import DeliveryCostCalculator


class StandardDeliveryCostCalculator(DeliveryCostCalculator):
    def calculate_cost(
        self,
        delivery_data,
        cost_config,
    ):
        distance_cost = cost_config.get_distance_cost(delivery_data.distance)
        size_cost = cost_config.get_size_cost(delivery_data.size)
        fragile_cost = cost_config.get_fragile_cost() if delivery_data.is_fragile else 0
        workload_coefficient = cost_config.get_workload_coefficient(
            delivery_data.workload
        )

        total_cost = (distance_cost + size_cost + fragile_cost) * workload_coefficient
        return max(total_cost, cost_config.min_cost)

class CostConfig:
    def __init__(
        self,
        distance_cost_ranges,
        size_costs,
        fragile_cost,
        workload_coefficients,
        min_cost,
    ):
        self.distance_cost_ranges = distance_cost_ranges
        self.size_costs = size_costs
        self.fragile_cost = fragile_cost
        self.workload_coefficients = workload_coefficients
        self.min_cost = min_cost

    def get_distance_cost(
        self,
        distance,
    ):
        for range_data in self.distance_cost_ranges:
            if range_data["min"] <= distance < range_data["max"]:
                return range_data["cost"]
        return self.distance_cost_ranges[-1]["cost"]

    def get_size_cost(
        self,
        size,
    ):
        return self.size_costs.get(size, 0)

    def get_fragile_cost(self):
        return self.fragile_cost

    def get_workload_coefficient(
        self,
        workload,
    ):
        return self.workload_coefficients.get(workload, 1)

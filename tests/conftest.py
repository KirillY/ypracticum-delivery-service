import pytest
from abstract_solution.config.cost_config import CostConfig

@pytest.fixture
def cost_config():
    distance_cost_ranges = [
        {"min": 0, "max": 2, "cost": 50},
        {"min": 2, "max": 10, "cost": 100},
        {"min": 10, "max": 30, "cost": 200},
        {"min": 30, "max": float("inf"), "cost": 300}
    ]
    size_costs = {
        "большой": 200,
        "маленький": 100
    }
    fragile_cost = 300
    workload_coefficients = {
        "очень высокая": 1.6,
        "высокая": 1.4,
        "повышенная": 1.2
    }
    min_cost = 400
    return CostConfig(
        distance_cost_ranges=distance_cost_ranges,
        size_costs=size_costs,
        fragile_cost=fragile_cost,
        workload_coefficients=workload_coefficients,
        min_cost=min_cost
    )
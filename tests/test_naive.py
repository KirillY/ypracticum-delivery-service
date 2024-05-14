import pytest

from naive.solution import calculate_delivery_cost


import pytest

@pytest.mark.parametrize("distance, size, is_fragile, workload, expected_result", [
    (40, "большие", True, "очень высокая", "Хрупкие грузы нельзя возить на расстояние более 30 км"),
    (25, "маленькие", True, "высокая", 840.0),
    (8, "большие", False, "повышенная", 400.0),
    (1, "маленькие", False, "обычная", 400.0),
    (35, "маленькие", False, "обычная", 400.0),
    (20, "большие", False, "очень высокая", 640.0),
    (5, "маленькие", True, "высокая", 700.0),
    (40, "большие", False, "повышенная", 600.0),
    (1, "большие", True, "обычная", 550.0),
    (15, "маленькие", False, "обычная", 400.0),
    (0, "маленькие", False, "обычная", 400.0),
    (-5, "маленькие", False, "обычная", 400.0),
    (30, "большие", True, "высокая", pytest.approx(980.0)),
    (35, "маленькие", True, "обычная", "Хрупкие грузы нельзя возить на расстояние более 30 км"),
    (1, "неизвестные", False, "обычная", 400.0),
    (5, "маленькие", False, "неизвестная", 400.0)
], ids=[
    "distance_over_30_fragile",
    "distance_below_30_fragile_high_workload",
    "distance_cost_below_400",
    "distance_below_2_small_size_normal_workload",
    "distance_over_30_small_size_normal_workload",
    "distance_below_30_large_size_very_high_workload",
    "distance_below_10_small_size_fragile_high_workload",
    "distance_over_30_large_size_increased_workload",
    "distance_below_2_large_size_fragile_normal_workload",
    "distance_below_30_small_size_normal_workload",
    "distance_zero_small_size_normal_workload",
    "distance_negative_small_size_normal_workload",
    "distance_30_large_size_fragile_high_workload",
    "distance_over_30_small_size_fragile_normal_workload",
    "distance_below_2_unknown_size_normal_workload",
    "distance_below_10_small_size_unknown_workload"
])
def test_calculate_delivery_cost(distance, size, is_fragile, workload, expected_result):
    assert calculate_delivery_cost(distance, size, is_fragile, workload) == expected_result
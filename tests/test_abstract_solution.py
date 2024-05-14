import pytest
from abstract_solution.services.delivery_service import DeliveryService
from abstract_solution.calculators.standard_calculator import (
    StandardDeliveryCostCalculator,
)
from abstract_solution.models.delivery_data import DeliveryData


@pytest.mark.parametrize(
    "delivery_data, expected_result",
    [
        # Normal cases
        (
            DeliveryData(
                distance=5,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=10,
                size="большой",
                is_fragile=True,
                workload="высокая",
            ),
            pytest.approx(980.0),
        ),
        (
            DeliveryData(
                distance=20,
                size="маленький",
                is_fragile=False,
                workload="повышенная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=40,
                size="большой",
                is_fragile=False,
                workload="очень высокая",
            ),
            800,
        ),
        (
            DeliveryData(
                distance=1,
                size="маленький",
                is_fragile=True,
                workload="обычная",
            ),
            450,
        ),
        # Edge cases
        # Distance
        (
            DeliveryData(
                distance=0,
                size="большой",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=2,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=10,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=30,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=100,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=-5,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        # Size
        (
            DeliveryData(
                distance=5,
                size="неизвестный",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        # Fragile
        (
            DeliveryData(
                distance=1,
                size="маленький",
                is_fragile=True,
                workload="обычная",
            ),
            450,
        ),
        (
            DeliveryData(
                distance=30,
                size="большой",
                is_fragile=True,
                workload="высокая",
            ),
            1120,
        ),
        (
            DeliveryData(
                distance=35,
                size="маленький",
                is_fragile=True,
                workload="обычная",
            ),
            "exception",
        ),
        # Workload
        (
            DeliveryData(
                distance=8,
                size="маленький",
                is_fragile=False,
                workload="неизвестная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=15,
                size="большой",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
        (
            DeliveryData(
                distance=15,
                size="большой",
                is_fragile=False,
                workload="повышенная",
            ),
            480,
        ),
        (
            DeliveryData(
                distance=15,
                size="большой",
                is_fragile=False,
                workload="высокая",
            ),
            560,
        ),
        (
            DeliveryData(
                distance=15,
                size="большой",
                is_fragile=False,
                workload="очень высокая",
            ),
            640,
        ),
        # Minimum cost
        (
            DeliveryData(
                distance=1,
                size="маленький",
                is_fragile=False,
                workload="обычная",
            ),
            400,
        ),
    ],
)
def test_delivery_service(
    cost_config,
    delivery_data,
    expected_result,
):
    """Test the delivery service with different delivery scenarios."""
    calculator = StandardDeliveryCostCalculator()
    delivery_service = DeliveryService(calculator, cost_config)

    if expected_result == "exception":
        with pytest.raises(ValueError):
            delivery_service.calculate_delivery_cost(delivery_data)
    else:
        assert (
            delivery_service.calculate_delivery_cost(delivery_data) == expected_result
        )

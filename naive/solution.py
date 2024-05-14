from typing import Union


def calculate_delivery_cost(
    distance: float,
    size: str,
    is_fragile: bool,
    workload: str,
) -> Union[float, str]:
    """Calculate the delivery cost based on distance, size, fragility, and workload."""
    # Расчет стоимости в зависимости от расстояния
    if distance <= 2:
        cost = 50
    elif distance <= 10:
        cost = 100
    elif distance <= 30:
        cost = 200
    else:
        cost = 300

    # Расчет стоимости в зависимости от габаритов груза
    if size == "большие":
        cost += 200
    elif size == "маленькие":
        cost += 100

    # Расчет стоимости в зависимости от хрупкости груза
    if is_fragile:
        if distance > 30:
            return "Хрупкие грузы нельзя возить на расстояние более 30 км"
        else:
            cost += 300

    # Расчет стоимости в зависимости от загруженности службы доставки
    if workload == "очень высокая":
        cost *= 1.6
    elif workload == "высокая":
        cost *= 1.4
    elif workload == "повышенная":
        cost *= 1.2

    # Проверка минимальной стоимости доставки
    if cost < 400:
        cost = 400

    return cost

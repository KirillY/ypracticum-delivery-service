from dataclasses import dataclass


@dataclass
class DeliveryData:
    distance: int
    size: str
    is_fragile: bool
    workload: str
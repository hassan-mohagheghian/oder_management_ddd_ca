from dataclasses import dataclass

from .money import Money


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price_per_unit: Money

    def total_price(self) -> Money:
        return self.price_per_unit * self.quantity

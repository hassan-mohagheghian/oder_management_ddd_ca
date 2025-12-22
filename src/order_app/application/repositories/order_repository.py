from abc import ABC, abstractmethod
from uuid import UUID

from order_app.domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def create(self, order: Order) -> None:
        """Save an order to the repository."""
        pass

    def update(self, order: Order) -> None:
        """Update an order in the repository."""
        pass

    def delete(self, order_id: UUID) -> None:
        """Delete an order from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Order:
        """
        Retrieve an order by its ID.

        Raises:
            OrderNotFoundError: If no order exists with the given ID
        """
        pass

    @abstractmethod
    def get_list(self, user_id: UUID | None = None) -> list[Order]:
        """Retrieve list of orders optionally filtered by specific user ID."""
        pass

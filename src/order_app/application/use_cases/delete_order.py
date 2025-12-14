from dataclasses import dataclass
from uuid import UUID

from order_app.domain.repositories import OrderRepository


@dataclass
class DeleteOrderRequest:
    order_id: UUID


@dataclass
class DeleteOrderUseCase:
    order_repository: OrderRepository

    def execute(self, request: DeleteOrderRequest) -> None:
        order = self.order_repository.get_by_id(request.order_id)
        if not order:
            raise ValueError(f"Order with ID {request.order_id} not found")
        self.order_repository.delete(request.order_id)

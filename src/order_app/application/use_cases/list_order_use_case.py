from dataclasses import dataclass
from uuid import UUID

from order_app.application.repositories import OrderRepository
from order_app.domain.entities.order import Order
from order_app.domain.entities.user import UserRole


@dataclass
class ListOrderRequest:
    user_id: UUID
    role: UserRole


@dataclass
class ListOrderUseCase:
    order_repository: OrderRepository

    def execute(self, request: ListOrderRequest) -> list[Order]:
        if request.role != UserRole.MANAGER:
            return self.order_repository.get_list(request.user_id)
        else:
            return self.order_repository.get_list()

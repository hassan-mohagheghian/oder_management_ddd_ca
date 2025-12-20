from uuid import UUID


class DomainError(Exception):
    """Base class for domain-specific errors."""

    pass


class OrderNotFoundError(DomainError):
    def __init__(self, order_id: UUID):
        self.order_id = order_id
        super().__init__(f"Order with ID {order_id} not found")


class ProductNotFoundError(DomainError):
    def __init__(self, order_id: UUID):
        self.order_id = order_id
        super().__init__(f"Product with ID {order_id} not found")


class InsufficientStockError(DomainError):
    def __init__(self, product_id: UUID):
        self.product_id = product_id
        super().__init__(f"Product with ID {product_id} is out of stock")


class InvalidUserRoleError(DomainError):
    def __init__(self, role: str):
        self.role = role
        super().__init__(f"Invalid user role: {role}")

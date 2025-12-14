from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from order_app.application.use_cases.delete_order import (
    DeleteOrderRequest,
    DeleteOrderUseCase,
)


@pytest.fixture
def order_repository():
    class MockOrderRepository:
        def __init__(self):
            self.get_by_id = MagicMock()
            self.delete = MagicMock()

    return MockOrderRepository()


def test_delete_existing_order(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    mock_order = MagicMock()
    order_repository.get_by_id.return_value = mock_order

    request = DeleteOrderRequest(order_id=order_id)

    use_case.execute(request)

    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_called_once_with(order_id)


def test_delete_non_existing_order_raises(order_repository):
    use_case = DeleteOrderUseCase(order_repository=order_repository)
    order_id = uuid4()
    order_repository.get_by_id.return_value = None

    request = DeleteOrderRequest(order_id=order_id)

    with pytest.raises(ValueError, match=f"Order with ID {order_id} not found"):
        use_case.execute(request)
    order_repository.get_by_id.assert_called_once_with(order_id)
    order_repository.delete.assert_not_called()

from unittest.mock import MagicMock

import pytest

from order_app.application.ports.password_hasher import PasswordHasher


# Application-level fixtures
@pytest.fixture
def password_hasher():
    class MockPasswordHasher(PasswordHasher):
        def hash(self, plain_password: str) -> str:
            return "password_hash"

        def verify(self, plain_password: str, hashed_password: str) -> bool:
            return plain_password == hashed_password

    return MockPasswordHasher()


# Domain-level fixtures
@pytest.fixture
def user_repository():
    class MockUserRepository:
        def __init__(self):
            self.save = MagicMock()
            self.get_by_id = MagicMock()
            self.get_by_email = MagicMock()

    return MockUserRepository()


@pytest.fixture
def order_repository():
    class MockOrderRepository:
        def __init__(self):
            self.save = MagicMock()
            self.delete = MagicMock()
            self.get_by_id = MagicMock()
            self.get_list = MagicMock()

    return MockOrderRepository()


@pytest.fixture
def product_repository():
    class MockProductRepository:
        def __init__(self):
            self.save = MagicMock()
            self.get_by_id = MagicMock()

    return MockProductRepository()

from unittest.mock import MagicMock

from order_app.application.common.result import ErrorCode
from order_app.application.dtos.user.login import LoginUserRequestDto
from order_app.application.use_cases.user.login import LoginUserUseCase
from order_app.domain.exception import UserNotFoundError


def test_login_user_user_not_found(user_repository, password_hasher):
    user_repository.get_by_email.side_effect = [UserNotFoundError]
    password_hasher.verify = MagicMock()
    use_case = LoginUserUseCase(
        user_repository=user_repository, password_hasher=password_hasher
    )

    result = use_case.execute(
        LoginUserRequestDto(email="email@test.com", password="password")
    )

    user_repository.get_by_email.assert_called_once_with(email="email@test.com")
    password_hasher.verify.assert_not_called()
    assert not result.is_success
    assert result.error.code == ErrorCode.DOMAIN
    assert result.error.message == "Invalid credentials"


def test_login_user_invalid_password(user_repository, password_hasher):
    user_repository.get_by_email.return_value.password_hash = "hashed_password"
    password_hasher.verify = MagicMock(return_value=False)
    use_case = LoginUserUseCase(
        user_repository=user_repository, password_hasher=password_hasher
    )

    result = use_case.execute(
        LoginUserRequestDto(email="email@test.com", password="password")
    )

    user_repository.get_by_email.assert_called_once_with(email="email@test.com")
    password_hasher.verify.assert_called_once_with(
        plain_password="password", hashed_password="hashed_password"
    )
    assert not result.is_success
    assert result.error.code == ErrorCode.DOMAIN
    assert result.error.message == "Invalid credentials"


def test_login_user(user_repository, password_hasher):
    user = MagicMock(password_hash="hashed_password")

    user_repository.get_by_email.return_value = user
    password_hasher.verify = MagicMock(return_value=True)
    use_case = LoginUserUseCase(
        user_repository=user_repository, password_hasher=password_hasher
    )

    result = use_case.execute(
        LoginUserRequestDto(email="email@test.com", password="password")
    )

    user_repository.get_by_email.assert_called_once_with(email="email@test.com")
    password_hasher.verify.assert_called_once_with(
        plain_password="password", hashed_password="hashed_password"
    )
    assert result.is_success
    assert result.value == user

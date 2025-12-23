from dataclasses import dataclass

from order_app.application.common.result import Error, Result
from order_app.application.dtos.user.login import LoginUserRequestDto
from order_app.application.ports.password_hasher import PasswordHasher
from order_app.application.repositories.user_repository import UserRepository
from order_app.domain.entities.user import User
from order_app.domain.exception import UserNotFoundError


@dataclass
class LoginUserUseCase:
    user_repository: UserRepository
    password_hasher: PasswordHasher

    def execute(self, request: LoginUserRequestDto) -> Result[User]:
        try:
            user = self.user_repository.get_by_email(email=request.email)
        except UserNotFoundError:
            return Result.failure(Error.domain("Invalid credentials"))
        verify_result = self.password_hasher.verify(
            plain_password=request.password, hashed_password=user.password_hash
        )
        if not verify_result:
            return Result.failure(Error.domain("Invalid credentials"))
        return Result.success(user)

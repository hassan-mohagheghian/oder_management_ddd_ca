from dataclasses import dataclass

from order_app.application.dtos.user_dtos import RegisterUserRequestDto
from order_app.application.use_cases.users.register_user import RegisterUserUseCase
from order_app.interface.common.operation_result import OperationResult
from order_app.interface.presenters.base.user import UserPresenter
from order_app.interface.view_models.user_vm import UserViewModel


@dataclass
class RegisterUserInputDto:
    name: str
    email: str
    password: str


@dataclass
class UserController:
    register_user_use_case: RegisterUserUseCase
    presenter: UserPresenter

    def handle_register_user(
        self, input: RegisterUserInputDto
    ) -> OperationResult[UserViewModel]:
        request_dto = RegisterUserRequestDto(
            name=input.name, email=input.email, password=input.password
        )

        result = self.register_user_use_case.execute(request_dto)

        if result.is_success:
            user_response = result.value
            user_view_model = self.presenter.present_user(user_response)
            return OperationResult.succeed(user_view_model)
        else:
            error_vm = self.presenter.present_error(
                result.error.message, result.error.code
            )
            return OperationResult.fail(error_vm.message, error_vm.code)

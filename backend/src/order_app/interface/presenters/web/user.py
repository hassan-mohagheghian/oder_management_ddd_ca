from order_app.application.dtos.user.login import LoginUserResponseDto
from order_app.application.dtos.user.register import (
    RegisterUserResponseDto,
    UserResponseDto,
)
from order_app.interface.presenters.base.user import LoginPresenter, RegisterPresenter
from order_app.interface.view_models.error_vm import ErrorViewModel
from order_app.interface.view_models.user_vm import (
    LoginUserViewModel,
    RegisterUserViewModel,
    TokensViewModel,
    UserViewModel,
)


class WebRegisterUserPresenter(RegisterPresenter):
    def present_success(
        self, user_response: RegisterUserResponseDto
    ) -> RegisterUserViewModel:
        return RegisterUserViewModel(
            user=UserViewModel(
                id=str(user_response.user.id),
                name=user_response.user.name,
                email=user_response.user.email,
                role=user_response.user.role,
            ),
            tokens=TokensViewModel(
                access_token=user_response.tokens.access_token,
            ),
        )

    def present_error(self, error, code=None) -> ErrorViewModel:
        return ErrorViewModel(error, str(code))


class WebLoginUserPresenter(LoginPresenter):
    def present_success(self, response: LoginUserResponseDto) -> LoginUserViewModel:
        return LoginUserViewModel(
            user=UserViewModel(
                id=str(response.id),
                name=response.name,
                email=response.email,
                role=response.role,
            ),
            access_token=response.access_token,
            expires_in=response.expires_in,
        )

    def present_error(self, error, code=None) -> ErrorViewModel:
        return ErrorViewModel(error, str(code))

from order_app.application.dtos.user_dtos import UserResponse
from order_app.interface.presenters.base.user import UserPresenter
from order_app.interface.view_models.error_vm import ErrorViewModel
from order_app.interface.view_models.user_vm import UserViewModel


class WebUserPresenter(UserPresenter):
    def present_user(self, user_response: UserResponse) -> UserViewModel:
        return UserViewModel(
            id=str(user_response.id),
            name=user_response.name,
            email=user_response.email,
            role=user_response.role,
        )

    def present_error(self, error, code=None) -> ErrorViewModel:
        return ErrorViewModel(error, str(code))

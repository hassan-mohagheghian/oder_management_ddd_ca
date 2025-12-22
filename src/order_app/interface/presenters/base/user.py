from abc import ABC, abstractmethod

from order_app.application.dtos.user_dtos import UserResponse
from order_app.interface.view_models.error_vm import ErrorViewModel
from order_app.interface.view_models.user_vm import UserViewModel


class UserPresenter(ABC):
    @abstractmethod
    def present_user(self, user_response: UserResponse) -> UserViewModel:
        pass

    @abstractmethod
    def present_error(self, error: str, code: str | None = None) -> ErrorViewModel:
        pass

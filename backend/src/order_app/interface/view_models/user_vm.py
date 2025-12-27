from dataclasses import dataclass, field
from typing import Literal


@dataclass
class UserViewModel:
    id: str
    name: str
    email: str
    role: str


@dataclass
class TokensViewModel:
    access_token: str
    # refresh_token: str


@dataclass
class RegisterUserViewModel:
    user: UserViewModel
    tokens: TokensViewModel


@dataclass
class LoginUserViewModel:
    user: UserViewModel
    access_token: str
    expires_in: int
    token_type: Literal["Bearer"] = field(default="Bearer")

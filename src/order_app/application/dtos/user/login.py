from dataclasses import dataclass


@dataclass(frozen=True)
class LoginUserRequestDto:
    email: str
    password: str

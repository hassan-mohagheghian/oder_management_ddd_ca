from dataclasses import dataclass


@dataclass
class UserViewModel:
    id: str
    name: str
    email: str
    role: str

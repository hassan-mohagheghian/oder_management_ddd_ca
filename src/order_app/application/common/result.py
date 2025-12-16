from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Generic, Optional, Self, TypeVar

T = TypeVar("T")  # Success type


class ErrorCode(Enum):
    """Enumeration of possible error codes in the application layer."""

    NOT_FOUND = auto()
    FORBIDDEN = auto()
    VALIDATION_ERROR = auto()


@dataclass(frozen=True)
class Error:
    """Represents an error that occurred during use case execution."""

    code: ErrorCode
    message: str
    details: Optional[dict[str, Any]] = None

    @classmethod
    def not_found(cls, entity: str, entity_id: str) -> Self:
        """Create a NOT_FOUND error for a specific entity."""
        return cls(
            code=ErrorCode.NOT_FOUND,
            message=f"{entity} with id {entity_id} not found",
        )

    @classmethod
    def forbidden(cls, entity: str, entity_id: str) -> Self:
        """Create a FORBIDDEN error."""
        return cls(
            code=ErrorCode.FORBIDDEN,
            message=f"You don't have permission to {entity} with id {entity_id}",
        )


@dataclass(frozen=True)
class Result(Generic[T]):
    """Represents the outcome of a use case execution as an Either type."""

    _value: Optional[T] = None
    _error: Optional[Error] = None

    def __post_init__(self):
        if (self._value is None and self._error is None) or (
            self._value is not None and self._error is not None
        ):
            raise ValueError(
                "Either value or error must be provided, but not both or neither"
            )

    @property
    def is_success(self) -> bool:
        """Check if the result represents a successful operation."""
        return self._value is not None

    @property
    def value(self) -> T:
        """Get the success value. Raises ValueError if result is an error."""
        if self._value is None:
            raise ValueError("Cannot access value on error result")
        return self._value

    @property
    def error(self) -> Error:
        """Get the error value. Raises ValueError if result is successful."""
        if self._error is None:
            raise ValueError("Cannot access error on success result")
        return self._error

    @classmethod
    def success(cls, value: T) -> Result[T]:
        """Create a successful result with the given value."""
        return cls(_value=value)

    @classmethod
    def failure(cls, error: Error) -> Result[T]:
        """Create a failed result with the given error."""
        return cls(_error=error)

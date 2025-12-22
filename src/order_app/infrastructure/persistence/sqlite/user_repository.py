from sqlite3 import IntegrityError

from order_app.application.repositories.user_repository import UserRepository
from order_app.domain.entities.user import User
from order_app.domain.exception import UserAlreadyExistsError, UserNotFoundError
from order_app.domain.value_objects.user_role import UserRole
from order_app.infrastructure.persistence.sqlite.db import get_connection


class SqliteUserRepository(UserRepository):
    def create(self, user: User) -> User:
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO users (id, name, email, password_hash, role)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    str(user.id),
                    user.name,
                    user.email,
                    user.password_hash,
                    user.role.name,
                ),
            )
            conn.commit()
        except IntegrityError as e:
            if "UNIQUE constraint failed: users.email" in str(
                e
            ) or "UNIQUE constraint failed: users.id" in str(e):
                raise UserAlreadyExistsError(user_id=user.id, email=user.email) from e
            else:
                raise e
        else:
            return user
        finally:
            conn.close()

    def update(self, user):
        return super().update(user)

    def get_by_email(self, email) -> User:
        con = get_connection()
        cursor = con.cursor()
        cursor.execute(
            """
        SELECT id, name, email, password_hash, role
        FROM users
        WHERE email = ?
        """,
            (email,),
        )

        row = cursor.fetchone()
        if row is None:
            raise UserNotFoundError(email=email)
        else:
            return User(
                id=row[0],
                name=row[1],
                email=row[2],
                password_hash=row[3],
                role=UserRole.from_str(row[4]),
            )

    def get_by_id(self, user_id):
        return super().get_by_id(user_id)

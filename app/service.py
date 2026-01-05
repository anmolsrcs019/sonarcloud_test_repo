from app.user import User
from app.utils import normalize_username


class UserService:
    def create_user(self, username: str, age: int) -> User:
        normalized = normalize_username(username)
        if age < 0:
            raise ValueError("Age cannot be negative")
        return User(username=normalized, age=age)

    def describe_user(self, user: User) -> str:
        status = "adult" if user.is_adult() else "minor"
        return f"User {user.username} is an {status}"
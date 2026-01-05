from dataclasses import dataclass


@dataclass
class User:
    username: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18
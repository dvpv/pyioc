from abc import ABC, abstractmethod
from typing import List
from user import User


class UserManager(ABC):
    users: List[User]

    @abstractmethod
    def load_users(self) -> None:
        pass

    @abstractmethod
    def save_users(self) -> None:
        pass

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_user(self, user: User) -> None:
        self.users = [u for u in self.users if u != user]

    def get_users(self) -> List[User]:
        return self.users

from user_manager import UserManager
from user import User
import json


class JsonUserManager(UserManager):
    __file: str

    def set_file(self, file: str) -> None:
        self.__file = file

    def load_users(self) -> None:
        encoded = json.load(open(self.__file, "r"))
        self.users = [User(name=u["name"], id=u["id"]) for u in encoded]

    def save_users(self) -> None:
        l = []
        for user in self.users:
            l.append(
                {
                    "name": user.name,
                    "id": user.id,
                }
            )
        json.dump(l, open(self.__file, "w"))

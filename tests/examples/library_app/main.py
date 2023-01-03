import pyioc
from user_manager import UserManager
from user import User


def main():
    context = pyioc.YAMLContext("config.yaml")
    user_manager = context.get_nut("UserManager")
    user_manager.load_users()
    users: list = user_manager.get_users()
    print(len(users))
    user_manager.add_user(User(name="Eu", id=0))
    users = user_manager.get_users()
    print(len(users))
    user_manager.save_users()
    user_manager.load_users()
    print(len(users))
    user_manager.remove_user(User(name="Eu", id=0))
    users = user_manager.get_users()
    print(len(users))
    user_manager.save_users()


if __name__ == "__main__":
    main()

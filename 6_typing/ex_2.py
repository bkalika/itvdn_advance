value: int = 10


class User:
    def __init__(self, f_name: str, l_name: str):
        self.f_name = f_name
        self.l_name = l_name


def create_new_user(f_name: str, l_name: str) -> User:
    return User(f_name=f_name, l_name=l_name)


user: User = create_new_user("Eugene", "Test")
create_new_user("Eugene", 10)

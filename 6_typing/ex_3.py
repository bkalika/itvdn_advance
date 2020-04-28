from typing import List


class User:
    def __init__(self, f_name: str, l_name: str):
        self.f_name = f_name
        self.l_name = l_name

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name


def create_users_v1(f_names: list, l_names: list) -> list:
    users = []
    items = zip(f_names, l_names)
    for f_name, l_name in items:
        users.append(User(f_name, l_name))
        return users


def create_users_v2(f_names: List[str], l_names: List[str]) -> List[User]:
    users = []
    items = zip(f_names, l_names)
    for f_name, l_name in items:
        users.append(User(f_name, l_name))
        return users


u1 = create_users_v2(['f1', 'f2'], ['l1', 'l2'])
u2 = create_users_v2(['f1', 10], [10, 'l2'])
u3 = create_users_v2(['f1', 'f2'], [[], 'l2'])
print(u2[0].get_full_name())

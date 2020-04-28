value = 10


class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


def create_new_user(f_name, l_name):
    print(f_name)
    return User(f_name=f_name, l_name=l_name)


u1 = create_new_user(value, value)
n2 = create_new_user("Test1", "Test2")
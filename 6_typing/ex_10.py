from typing import TypeVar, Dict, ClassVar


class User:
    meta: ClassVar[Dict[str, int]]

    def __init__(self, f_name: str, l_name: str):
        self.f_name = f_name
        self.l_name = l_name


user = User("test", "test2")
# user.meta = {}
User.meta = {}


class A:
    def foo(self, instance: 'B'):
        pass


class B:
    def foo(self, instance: 'A'):
        pass


a1 = A()
b1 = B()

b1.foo(a1)
a1.foo(b1)

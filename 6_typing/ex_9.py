from typing import TypeVar, Dict

T = TypeVar('T')

TemplateDict = Dict[str, T]
IntDict = TemplateDict[int]  # Dict[str, int]
StrDict = TemplateDict[str]  # Dict[str, str]


def handler1(value: TemplateDict[T]) -> T:
    return list(value.values())[0]


def handler2(value: IntDict) -> int:
    return list(value.values())[0]


v1: int = handler1({'test': 10})
v2: str = handler1({'test': "10"})
v3: list = handler1({'test': []})
v4: int = handler2({'test': 10})
v5: int = handler2({'test': "10"})

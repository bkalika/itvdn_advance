from typing import TypeVar, List, Sequence, Iterable

IntOrStr = TypeVar('IntOrStr', int, str, float)


def copy_list(sequence: Iterable[IntOrStr]) -> List[IntOrStr]:
    new_list: List[IntOrStr] = []
    for elem in sequence:
        new_list.append(elem)
    return new_list


t_v1 = copy_list([1, 2, 3])
t_v2 = copy_list([1, 2, 9])
t_v3 = copy_list([1.3, 2.1, 3])
t_v4 = copy_list(["str", "rst", "str"])

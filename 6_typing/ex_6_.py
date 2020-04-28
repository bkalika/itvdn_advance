from typing import TypeVar, List, Tuple, Sequence, Iterable

T = TypeVar('T')


def copy_list(sequence: Iterable[Tuple[str, T]]) -> List[T]:
    new_list: List[T] = []
    for elem in sequence:
        new_list.append(elem[1])
    return new_list


t_data = [
    ('1', 10),
    ('1', 10),
    ('1', 'tk'),
]


t_v0 = copy_list(t_data)
t_v1 = copy_list([1, 2, 3])
t_v2 = copy_list([1, 2, 9])
t_v3 = copy_list([1.3, 2.1, 3])
t_v4 = copy_list(["str", "rst", "str"])

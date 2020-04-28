from typing import Dict, Tuple, List


def generate_tuple(data) -> dict:
    result = []
    for key, value in data.items():
        result.append((key, value))
    return result


t_data1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
t_data2 = {'k1': 'v1', 'k2': 'v2', 'k3': 10}
t_data3 = {'k1': 'v1', 'k2': 'v2', 'k3': 10.5}
t_data4 = {'k1': 'v1', 'k2': 'v2', 'k3': []}

t_value1 = generate_tuple(t_data1)  # type: Tuple[str, str]
t_value2 = generate_tuple(t_data2)  # type: Dict[str, int]
t_value3 = generate_tuple(t_data3)  # type: List
t_value4 = generate_tuple(t_data4)  # type: dict

another_value = '10'  # type: str

from typing import Dict, Tuple, List

test_value: Dict[str, float] = {
    'v1': 10.2,
    'v2': 10.2,
    'v3': 10.2,
}


def generate_tuple(data: Dict[str, str]) -> List[Tuple[str, str]]:
    result = []
    for key, value in data.items():
        result.append((key, value))
    return result


t_data1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
t_data2 = {'k1': 'v1', 'k2': 'v2', 'k3': 10}
t_data3 = {'k1': 'v1', 'k2': 'v2', 'k3': 10.5}
t_data4 = {'k1': 'v1', 'k2': 'v2', 'k3': []}

t_value1 = generate_tuple(t_data1)
t_value2 = generate_tuple(t_data2)
t_value3 = generate_tuple(t_data3)
t_value4 = generate_tuple(t_data4)

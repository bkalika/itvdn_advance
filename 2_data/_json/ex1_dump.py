import json
data = {
    'first_name': 'Bohdan',
    'last_name': 'Kalika',
    'age': 24,
    'hobbies': [
        'running',
        'music',
        'codding',
    ]
}

json_data = json.dumps(data)
print(json_data)

with open('data/output.json', 'w') as f:
    json.dump(data, f, indent=4)

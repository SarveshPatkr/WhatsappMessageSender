import json

def find_phone_number(name, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        if item['name'] == name:
            return item['phone']
    return None

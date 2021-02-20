import json

python_dict = {"name": "Jim and Por", "age": 26, "city": "Bangkok"}

json_string = json.dumps(python_dict)

print(json_string)
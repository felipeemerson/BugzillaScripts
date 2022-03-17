import json

file = "json_data_bugs_id.json"

with open(file) as json_file:
    data = json.load(json_file)

print(len(data))
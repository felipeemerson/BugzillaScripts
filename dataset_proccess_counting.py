import json

with open('json_data_bugs_finished.json') as input:
    bugs = json.load(input)

#print(json.dumps(bugs[0], indent=4, sort_keys=True))

working_fields = ["status", "resolution", "priority", "severity", "summary", "product", "component", "classification", "cc", "comment_count", "votes", "is_open", "assigned_to"]

bugs_with_count_fields = []

for i in range(0, len(bugs)):
    history = bugs[i]['history']

    bug = {}

    for field in working_fields:
        bug[field] = 0

    bug['id'] = bugs[i]['id']

    for changes in history:
        for change in changes['changes']:
            if change['field_name'] in working_fields:
                bug[change['field_name']] += 1

    bugs_with_count_fields.append(bug)


with open('json_data_bugs_processed.json', 'w') as outfile:
    json.dump(bugs_with_count_fields, outfile)

#print(bugs_with_count_fields)
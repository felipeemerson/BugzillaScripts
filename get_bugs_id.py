import json
import requests

# Set your Bugzilla API key
api_key=""
headers = { "X-BUGZILLA-API-KEY": api_key }

# Only return bugs' id
url = "https://bugzilla.mozilla.org/rest/bug?include_fields=id&bug_status=RESOLVED&chfield=%5BBug%20creation%5D&chfieldfrom=2019-01-02&chfieldto=2021-12-31&classification=Client%20Software&classification=Developer%20Infrastructure&classification=Components&classification=Server%20Software&classification=Other&product=Firefox&resolution=FIXED"

response = requests.get(
    url,
    headers=headers
)

data = response.json()
bugs = data['bugs']

#print(bugs)

# Write on an outfile
with open('json_data_bugs_id.json', 'w') as outfile:
    json.dump(bugs, outfile)
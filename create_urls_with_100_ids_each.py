import json

# Modify to include fields that you want
base_url = "https://bugzilla.mozilla.org/rest/bug?include_fields=id,history&id="

with open('json_data_bugs_id.json') as json_file:
    data = json.load(json_file)

urls = []

# For each 100 bugs, creates a single url to retrieve them.
# Obs: This loop was made considering that exists 10K bugs id.
# So, if bugs id quantity is different, maybe need to modify range and
# include a condition on inner loop
for i in range (0,10000, 100):
    url_with_ids = base_url
    ids_conc = ""

    for j in range(i, i+100):
        ids_conc += str(data[j]['id']) + ","
    
    urls.append((url_with_ids + ids_conc)[:-1]) # Add url to urls, and eliminate a ',' at the final of the url

# An outfile that includes 100 urls that each one retrieves 100 bugs (100x100 = 10K)
with open('json_urls_with_100ids.json', 'w') as outfile:
    json.dump(urls, outfile)
from threading import Thread
from queue import Queue
import json
import requests
import sys

# Set your Bugzilla API key
api_key=""
headers = { "X-BUGZILLA-API-KEY": api_key }

concurrent = 100

bugs = []

def doWork():
    while True:
        url, index = q.get()

        response = requests.get(
            url,
            headers=headers
        )

        data = response.json()

        print(index)

        for bug in data['bugs']:
            bugs.append(bug)


        q.task_done()


q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    with open('json_urls_with_100ids.json') as input_file:
        urls = json.load(input_file)
    
    for i in range(0, len(urls)):
        q.put([urls[i], i])
    q.join()
except KeyboardInterrupt:
    sys.exit(1)

# Outfile with bugs retrieveds
with open('json_data_bugs_finished.json', 'w') as outfile:
    json.dump(bugs, outfile)
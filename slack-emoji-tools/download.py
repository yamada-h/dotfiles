import os
import sys
import time
from dotenv import load_dotenv, find_dotenv
from slackclient import SlackClient
import requests

load_dotenv(find_dotenv())
token = os.environ['SLACK_API_TOKEN']
slack = SlackClient(token)
res = slack.api_call('emoji.list')
if res['ok'] == False:
    print('API Fail')
    sys.exit(1)

if not os.path.exists('images'):
    os.mkdir('images')

for name, url in res['emoji'].items():
    if url.startswith('alias'):
        print('Skip alias: %s' % name)
        continue

    r = requests.get(url)
    if r.status_code != 200:
        print('GET Error')
        sys.exit(1)
    fn = 'images/%s.%s' % (name, url.split('/')[-1].split('.')[-1])
    if os.path.exists(fn):
        print('Skip exist file: %s' % fn)
        continue
    with open(fn, 'wb') as f:
        f.write(r.content)
    print(name)
    time.sleep(0.1)

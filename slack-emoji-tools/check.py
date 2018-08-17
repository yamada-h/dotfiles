import os
import sys
import json

from dotenv import load_dotenv, find_dotenv
from slackclient import SlackClient

from models import EmojiList, Session

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
print(current_dir)

load_dotenv(find_dotenv())
token = os.environ['SLACK_API_TOKEN']
slack = SlackClient(token)
res = slack.api_call('emoji.list')
if res['ok'] == False:
    print('API Fail')
    sys.exit(1)

session = Session()
data = json.dumps(res['emoji'])
el = EmojiList(data=data)
session.add(el)
session.commit()
print(el.id)
session.close()

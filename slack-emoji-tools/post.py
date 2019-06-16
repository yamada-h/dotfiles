import os
from datetime import datetime, timedelta
import json

import pytz
from dotenv import load_dotenv, find_dotenv
from slackclient import SlackClient

from models import EmojiList
from models import Session

load_dotenv(find_dotenv())

UTC = pytz.utc
JST = pytz.timezone('Asia/Tokyo')

session = Session()
els = session.query(EmojiList).all()

now = JST.localize(datetime.now()).astimezone(UTC)
dt = now-timedelta(days=8)

q = session.query(EmojiList)
q = q.filter(EmojiList.created_at >= dt.strftime('%Y-%m-%d'))
q = q.order_by(EmojiList.created_at)
els = q.all()

d0 = set(json.loads(els[0].data))
d1 = set(json.loads(els[-1].data))

emojis = sorted(list((d1-d0)))

def post(msg):
    channel = '#devnull'
    #channel = '#botplayground'
    icon_emoji = ':innocent:'
    username = 'emoji bot'
    slack.api_call(
        'chat.postMessage',
        channel=channel,
        icon_emoji=icon_emoji,
        username=username,
        text=msg)

token = os.environ['SLACK_API_TOKEN']
slack = SlackClient(token)
msg1 = "新着絵文字のお知らせ"
post(msg1)

for i in range((len(emojis)-1)//23+1):
  msg2 = ':'+'::'.join(emojis[i*23:(i+1)*23])+':'
  post(msg2)

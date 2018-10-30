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

new_emojis = ':'+'::'.join(sorted(list((d1-d0))))+':'
msg1 = "新着絵文字のお知らせ"
msg2 = new_emojis

token = os.environ['SLACK_API_TOKEN']
slack = SlackClient(token)

def post(msg):
    channel = '#general'
    #channel = '#botplayground'
    icon_emoji = ':innocent:'
    username = 'emoji bot'
    slack.api_call(
        'chat.postMessage',
        channel=channel,
        icon_emoji=icon_emoji,
        username=username,
        text=msg)

post(msg1)
post(msg2)

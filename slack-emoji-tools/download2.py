import os
import sys
import time
import json
import requests
from models import Session, EmojiList

if not os.path.exists('images'):
    os.mkdir('images')

session = Session()
q = session.query(EmojiList)
emoji = json.loads(q.all()[-1].data)

for name, url in emoji.items():
    if url.startswith('alias'):
        #print('Skip alias: %s' % name)
        continue

    r = requests.get(url)
    if r.status_code != 200:
        print('GET Error: %s' % url)
        continue
        #sys.exit(1)
    fn = 'images/%s.%s' % (name, url.split('/')[-1].split('.')[-1])
    if os.path.exists(fn):
        #print('Skip exist file: %s' % fn)
        continue
    with open(fn, 'wb') as f:
        f.write(r.content)
    print(name)
    time.sleep(0.1)

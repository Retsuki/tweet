import urllib
from requests_oauthlib import OAuth1Session
import requests
import sys
import os
import datetime
import json
import datetime

CK = os.environ.get("CK")
CS = os.environ["CS"]
AT = os.environ["AT"]
ATS = os.environ["ATS"]

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

tweet_list = [
    "応募待ってます！ by Scheeme株式会社\n#wantedly\nhttps://www.wantedly.com/projects/754839?utm_source=t.co&utm_medium=share&lang=en ",
    "応募待ってます！ by Scheeme株式会社\n#wantedly\nhttps://www.wantedly.com/projects/754835?utm_source=t.co&utm_medium=share&lang=en "
]

dt_now = datetime.datetime.now()
params = {
    "status": tweet_list[0] if dt_now.day % 2 == 0 else tweet_list[1]
}
res = twitter.post(url, params=params)

if res.status_code == 200:
    print("SUCCESS")
else:
    print(res)

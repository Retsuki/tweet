import urllib
from requests_oauthlib import OAuth1Session
import requests
import sys
import os
import datetime

CK = os.environ.get("CK")
CS = os.environ["CS"]
AT = os.environ["AT"]
ATS = os.environ["ATS"]

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

dtNow = datetime.datetime.now() + datetime.timedelta(hours=9)
tweet = "おはよんよん！！" + dtNow.strftime('%Y年%m月%d日 %H:%M:%S')

params = {
    "status": tweet
}

res = twitter.post(url, params=params)

if res.status_code == 200:
    print("SUCCESS")
else:
    print(res)

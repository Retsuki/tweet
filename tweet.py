import urllib
from requests_oauthlib import OAuth1Session
import requests
import sys
import os
import datetime
import json

CK = os.environ.get("CK")
CS = os.environ["CS"]
AT = os.environ["AT"]
ATS = os.environ["ATS"]

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

tweet = "おはよんよん！！\n本日の石川県の新型コロナウイルス感染者の状況です。\n#石川県\n#石川県コロナ\n#石川県コロナウイルス\nhttps://covid19-ishikawa.com/"
params = {
    "status": tweet,
}
res = twitter.post(url, params=params)

if res.status_code == 200:
    print("SUCCESS")
else:
    print(res)

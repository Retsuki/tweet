import urllib
from requests_oauthlib import OAuth1Session
import requests
import sys
import os

CK = os.environ["CK"]
CS = os.environ["CS"]
AT = os.environ["AT"]
ATS = os.environ["ATS"]

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

tweet = "おはよんよん！！"

params = {
    "status": tweet
}

res = twitter.post(url, params=params)

if res.status_code == 200:  # 正常投稿出来た場合
    print("SUCCESS")
else:  # 正常投稿出来なかった場合
    print("FAIRURE : %d" % res.status_code)

import urllib
from requests_oauthlib import OAuth1Session
import requests
import sys

CK = "pCBRAhfzS6ADpMN4T2K6mtwEx"
CS = "dPjCLvLZJRbr1KCVCHiWpaXElaQURSL2zz23zRu6EXyU1VQyag"
AT = "801345492693164032-XLt0Gs9x6NBz8ousEB0QVynJ3ZnroAh"
ATS = "ESY4u6ENZ7z7gP5ma1FSFEJj3734Cgvcja0v3FqAm6tSb"

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

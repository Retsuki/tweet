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
url_media = "https://upload.twitter.com/1.1/media/upload.json"
img_url = "https://ishikawacorona.s3-ap-northeast-1.amazonaws.com/readmeishikawa.png"

response = urllib.request.urlopen(img_url)
data = response.read()
files = {"media": data}
req_media = twitter.post(url_media, files=files)

# media_id を取得
media_id = json.loads(req_media.text)['media_id']

tweet = "おはよんよん！！\n本日の石川県の新型コロナウイルス感染者の状況です。\n https://ishikawa-covid19.netlify.com/"
params = {
    "status": tweet,
    "media_ids": [media_id]
}
res = twitter.post(url, params=params)

if res.status_code == 200:
    print("SUCCESS")
else:
    print(res)

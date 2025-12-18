# poster/twitter.py
import requests
from requests_oauthlib import OAuth1
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
)

def post_to_twitter(text):
    url = "https://api.twitter.com/2/tweets"

    auth = OAuth1(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )

    payload = {"text": text}
    response = requests.post(url, auth=auth, json=payload)

    if response.status_code != 201:
        raise Exception(f"{response.status_code}: {response.text}")


    return response.json()

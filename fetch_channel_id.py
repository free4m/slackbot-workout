'''
A quick script to fetch the id of a channel you want to use.

USAGE: python fetchChannelId.py <channel_name>
'''

import requests
import sys
import os
import json
from dotenv import load_dotenv

# Environment variables must be set with your tokens
load_dotenv()
USER_TOKEN_STRING = os.environ['SLACK_USER_TOKEN_STRING']
URL_TOKEN_STRING = os.environ['SLACK_URL_TOKEN_STRING']

HASH = "%23"

channelName = sys.argv[1]

params = {"token": USER_TOKEN_STRING, "types": "public_channel,private_channel"}

# Capture Response as JSON
response = requests.get("https://slack.com/api/conversations.list", params=params)
# print(json.loads(response.text))
channels = json.loads(response.text)["channels"]

for channel in channels:
    if channel["name"] == channelName:
        print(channel["id"])
        break

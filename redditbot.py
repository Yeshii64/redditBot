#this is a bot to help me get familiar with python and stuff
#Yeshua
#April 6,2025

import praw
from configparser import ConfigParser

config = ConfigParser()
#finallyyy it worked, using a ini file so that my info doesnt get leaked
path = r"C:\Users\qyut1\OneDrive\Desktop\reddit bot\redditBot\praw.ini"
config.read(path)
print(config.read(path))
def main():
    reddit = praw.Reddit(
        username=config["BOT1"]["username"],
        user_agent=config["BOT1"]["user_agent"],
        client_id=config["BOT1"]["client_id"],
        client_secret=config["BOT1"]["client_secret"],
        password=config["BOT1"]["password"]
    )
    return reddit

print(reddit)

subreddit = reddit.subreddit("learnpython")
for submission in subreddit.stream.submissions():
    print(submission.title)



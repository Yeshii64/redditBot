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
print(config.sections())
print( config["BOT1"]["username"])


#testing 
#for submission in reddit.submission("test").hot(limit=10):
 #   print(submission.title)
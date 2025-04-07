#this is a bot to help me get familiar with python and stuff
#Yeshua
#April 6,2025

import praw

reddit = praw.Reddit(
    client_id ="Me_AgYAzt6DcpRjFZYo8kw",
    client_secret ="-7HHxvEIZeqLIKHCJ-dXB_7pfZ-vQw",
    user_agent =("Yeshua's bot 0.1 - by /u/b0at56, and github.com/Yeshii64/redditBot"),
    username = "b0at56",
    password = "redditisgreat64!",
)

print(reddit.read_only)
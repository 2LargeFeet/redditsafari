#!/usr/bin/python
import praw
import linecache
import os

os.chdir('/opt/redditsafari/')

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('/opt/redditsafari/daily_list.txt','r')]
trimmed_file = "/opt/redditsafari/daily_list_trimmed.txt"

if os.path.isfile(trimmed_file):
    os.remove(trimmed_file)

for i in nations:
    subreddit = reddit.subreddit(i)
    if subreddit.subscribers > 100:
        with open(trimmed_file,'a+') as trimmed:
            trimmed.write(i+'\n')

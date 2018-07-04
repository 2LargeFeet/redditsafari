#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('/opt/redditsafari/daily_list_trimmed.txt','r')]

for i in nations:
    subreddit = reddit.subreddit(i)
    for submission in subreddit.hot(limit=1):
        reddit.submission(submission.id).crosspost(subreddit="redditsafari")

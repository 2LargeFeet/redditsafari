#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('daily_list.txt','r')]
#nations_str = ''.join(nations)

for i in nations:
    subreddit = reddit.subreddit(i)
    for submission in subreddit.hot(limit=1):
        reddit.submission(submission.id).crosspost(subreddit="redditsafari")

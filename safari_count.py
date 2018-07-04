#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('daily_list.txt','r')]
#nations_str = ''.join(nations)

#print reddit.subreddit('daventry').subscribers

for i in nations:
    subreddit = reddit.subreddit(i)
    print subreddit.subscribers

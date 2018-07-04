#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('daily_list.txt','r')]

#nations_str = ''.join(nations)

#print reddit.subreddit('daventry').subscribers

#for i in nations:
#    subreddit = reddit.subreddit(i)
#    print subreddit.subscribers

def deleteContent():
    with open('daily_list_trimmed.txt', "w"):
        pass

for i in nations:
    subreddit = reddit.subreddit(i)
    if subreddit.subscribers > 100:
        with open('daily_list_trimmed.txt','a') as trimmed:
            trimmed.write(i+'\n')

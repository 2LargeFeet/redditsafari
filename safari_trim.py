#!/usr/bin/python
import praw
import linecache
import os

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('/opt/redditsafari/daily_list.txt','r')]
trimmed_file = "/opt/redditsafari/daily_list_trimmed.txt"
#nations_str = ''.join(nations)

#print reddit.subreddit('daventry').subscribers

#for i in nations:
#    subreddit = reddit.subreddit(i)
#    print subreddit.subscribers

#def deleteContent():
#    with open(trimmed_file, "w"):
#        pass

#def deleteContent(trimmed_file):
#    with open(trimmed_file, "w"):
#        pass
if os.path.isfile(trimmed_file):
    os.remove(trimmed_file)

for i in nations:
    subreddit = reddit.subreddit(i)
    if subreddit.subscribers > 100:
        with open(trimmed_file,'a+') as trimmed:
            trimmed.write(i+'\n')

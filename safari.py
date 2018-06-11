#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('daily_list.txt','r')]
#nations_str = ''.join(nations)

for i in nations:
    subreddit = reddit.subreddit(i)
    for submission in subreddit.top(limit=1):
#        print("Title: ", submission.title)
#        print("Text: ", submission.selftext)
#        post = reddit.submission(submission.id)
#         cross_post =
#        for i in post:
#        print(post.crosspost)
        reddit.submission(submission.id).crosspost(subreddit="redditsafari")
#        post.crosspost(subreddit="redditsafari")
#        print("---------------------------------\n")

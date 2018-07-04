#!/usr/bin/python
import praw
import linecache

reddit = praw.Reddit('bot1')
nations = [line.rstrip() for line in open('daily_list.txt','r')]
#nations_str = ''.join(nations)

for i in nations:
    subreddit = reddit.subreddit(i)
    for submission in subreddit.top(limit=2):
      def get_date(submission):
        time = submission.created
        print time
#        return datetime.datetime.fromtimestamp(time)

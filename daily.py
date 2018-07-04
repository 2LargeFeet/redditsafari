#!/usr/bin/python
import random
import linecache

list = [line.rstrip() for line in open('/opt/redditsafari/world.txt')]
line_count = len(list)
daily_list = open('/opt/redditsafari/daily_list.txt', 'w')

def random_lines(filename):
    daily = random.sample(range(line_count), 10)
    return [linecache.getline(filename, i) for i in daily]

for line in random_lines('/opt/redditsafari/world.txt'):
    daily_list.write(line)

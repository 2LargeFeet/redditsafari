#!/usr/bin/python
import random
import linecache

list = [line.rstrip() for line in open('world.txt')]
line_count = len(list)
daily_list = open('daily_list.txt', 'w')

def random_lines(filename):
    daily = random.sample(range(line_count), 4)
    return [linecache.getline(filename, i) for i in daily]

for line in random_lines('world.txt'):
    daily_list.write(line)

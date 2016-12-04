# Micropython Http Server
# Erni Tron ernitron@gmail.com
# Copyright (c) 2016

import time
import json

class Ranges():

  def __init__(self):
      self.ranges = []

  def set(self, config_ranges):
    self.ranges = []
    for r in config_ranges.split(','):
        startend = r.split('-')
        try:
            start = int(startend[0])
            end = int(startend[1])
        except:
            print('skip range ', startend)
            continue

        if start > end: continue
        self.ranges.append([start, end])

  def inrange(self):
    #Get time now
    (y, m, d, h, mm, s, c, u, _) = time.localtime()

    for s, e in self.ranges:
       if e < s: continue
       if h in range(s,e):
            print('ON')
            return True
    print('OFF')
    return False


# Range initialized to None
ranges = None



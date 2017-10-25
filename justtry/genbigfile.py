
#!/usr/bin/env python

from __future__ import print_function

import os

# limit in codecommit is 2252341248.


import datetime

class Stopwatch(object):
    """A simple timer class"""

    def __init__(self):
        pass

    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start

    def stop(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return message + str(self.stop - self.start)

    def now(self, message="Now: "):
        """Returns the current time with a message"""
        return message + ": " + str(datetime.datetime.now())

    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        return message + str(datetime.datetime.now() - self.start)

    def split(self, message="Split started at: "):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return message + str(self.split_start)

    def unsplit(self, message="Unsplit: "):
        """Stops a split. Returns the time elapsed since split was called"""
        return message + str(datetime.datetime.now() - self.split_start)


s1 = Stopwatch()
s1.start()
s = ""
# for i in range (1, 10000009):
#     s += "100000000010000000001000000000100000000010000000001000000000100000000010000000001000000000100000000010000000001000000000,,"


p = os.path.expanduser("~/temp/b12.txt")
p = os.path.expandvars(p)
print (p)

f = open("/Users/jiezhong.mo/temp/bigfile.txt", "w")
print(s, file=f)

f.close()

# print(s)

print (s1.stop())
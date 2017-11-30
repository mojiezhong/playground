#!/usr/bin/env python
# -*- coding: utf-8 -*-


import string
import datetime
import m1
import tempfile

print "ello"

m1.show()


#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print args.accumulate(args.integers)


def fm ():
    return 1,2



class data:
    def __init__(self, value):
        self.value = value
        self.timestamp = datetime.datetime.now()

    def is_expired(self):
        print (datetime.datetime.now() - self.timestamp).total_seconds()
        return True

class Xx:
    def __init__(self):
        self.y = "whatis this"
        self.x = 123123



print ("{} : {} => {}".format(Xx(), "test", None))


x = {}
n = 5
for i in range (1, n):
    x[i] = data(i + 1)

for i in range (1, n):
    print (x[i].value)
    print (x[i].is_expired())



for i in range (1, n):
    u = x[i]
    u.value=i * 2

for i in range(1, n):
    print (x[i].value)
    print (x[i].is_expired())

d = data(123)

print (d.is_expired())

x,y = fm()
z = fm()
print (fm(), type(x), y, type(z))
f = string.Formatter()
print (f.format('{0} {1}', 'test', 123))


merge_message = u'tewtte中国字'

with tempfile.NamedTemporaryFile() as merge_message_file:
    merge_message_file.write(merge_message.encode('utf-8'))
    merge_message_file.flush()



    print merge_message_file.name


x = '''
a 
{}{}
'''.format(2,53)
print (x)




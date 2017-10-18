


import string

import m1

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


x,y = fm()
z = fm()
print (fm(), type(x), y, type(z))
f = string.Formatter()
print (f.format('{0} {1}', 'test', 123))
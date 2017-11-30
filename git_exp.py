
#!/usr/bin/env python

from __future__ import print_function

import xml.etree.ElementTree as xml
import argparse
import os
import datetime
from subprocess import call


def main():
    t = str(datetime.datetime.now().second + datetime.datetime.now().hour * 60)
    for i in range(400, 100000):
        branchName = "jiezhong_secondary_" + t + '_'+ str(i)

        call(['git', 'checkout', '-b', branchName])
        # call(['git','add', '.'])
        # call(['git', 'commit', '-m', "For baranch " + branchName])
        call(['git', 'push', 'origin', branchName])
        call(['git', 'checkout', 'master'])

if __name__ == "__main__":
    main()



#
# for mapping in root.findall('project/Properties'):
#     for prop in mapping.findall('.'):
#         print(prop)
#





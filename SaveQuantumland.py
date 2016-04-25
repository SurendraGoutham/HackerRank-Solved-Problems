'''
Created on 17-Feb-2015

@author: 00003179
'''

#!/bin/python


t = int(raw_input().strip())
for a0 in xrange(t):
    sumi = 0
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    for i in range(0, len(a) - 1):
        if a[i] == 0:
            try:
                if a[i + 1] == 0 and n-1 != sumi+1:
                    sumi = sumi + 1
                    if a[i + 2] == 0:
                        a[i + 1] = 1
            except IndexError:
                a[i + 1] = 1
                m = 0
    print a
    print sumi

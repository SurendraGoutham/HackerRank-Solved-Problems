'''
Created on 10-Apr-2015

@author: 00003179
'''

T= int(input())
res = []
for _ in xrange(T):
    minimum, maximum = raw_input().split()
    minimum = int(minimum)
    maximum = int(maximum)
    million  = 10 ** 6
    test = 0
    for each in xrange(minimum,maximum+1):
        test = test  + 10 ** each 
    if test > million: res.append("YES")        
    else: res.append("NO")

print '\n'.join(map(str, res))


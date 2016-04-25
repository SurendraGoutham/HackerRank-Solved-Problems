'''
Created on 01-Aug-2014

@author: 00003179
'''
'''
def getMultiples(num,limit):
    p = (limit - 1) / num;
    return num * (p * (p + 1)) / 2
'''


def getMulti(k, n):
    m = (k-1) // n
    return n * m * (m+1) // 2

def getRes(limit):
    return (getMulti(limit, 3) + 
            getMulti(limit, 5) - 
            getMulti(limit, 15))

t = input()
ar = []
for i in range(t):
    limit = input()
    ar.append((getRes(limit) + getRes(limit)) - getRes(limit))
print "\n".join(map(str,ar))




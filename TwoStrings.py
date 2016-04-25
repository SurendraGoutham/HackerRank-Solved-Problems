'''
Created on 26-Feb-2015

@author: 00003179
'''

def isExists(A,B):
    for each in A:
        if each in B: return "YES"
    return "NO"

T = input()
res = []
for _ in xrange(T):
    A = raw_input()
    B = raw_input()
    A = list(set(A))
    B = list(set(B))
    res.append(isExists(A,B))

print '\n'.join(map(str, res))
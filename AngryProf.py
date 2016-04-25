'''
Created on 26-Feb-2015

@author: 00003179
'''



def getClassStatus(times,K):
    if times[K-1] > 0:return "YES"
    else: return "NO"

T = input()
res = []
for _ in xrange(T):
    N, K = raw_input().split()
    N = int(N)
    K = int(K)
    times = map(int, raw_input().strip().split(" "))
    res.append(getClassStatus(sorted(times),K))

print '\n'.join(map(str, res))
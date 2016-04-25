'''
Created on 10-Feb-2015

@author: 00003179
'''

def getHandShakes(n):    
    return (n * (n-1)) / 2
    

T = input()
res = []
for i in range(T):
    N = input()
    res.append(getHandShakes(N))
print '\n'.join(map(str, res))


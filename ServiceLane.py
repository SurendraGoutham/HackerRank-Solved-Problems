'''
Created on 30-Jul-2014

@author: 00003179
'''


def serviceLane(L,i,j):
    temp = []
    for k in range(i,j+1):
        temp.append(L[k])
    return min(temp)

if __name__ == '__main__':
    res = []
    n, T = map(int, raw_input().split())
    L = map(int, raw_input().strip().split(" "))    
    for t in range(0,T):
        i, j = map(int, raw_input().split())
        res.append(serviceLane(L,i,j))
    print '\n'.join(map(str, res))


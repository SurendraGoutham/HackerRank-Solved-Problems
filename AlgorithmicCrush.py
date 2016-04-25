'''
Created on 17-Feb-2015

@author: 00003179
'''


def getmaximum():
    N,M = raw_input().split()
    N = int(N)
    M = int(M)
    listy = []
    for i in xrange(0,M):
        a,b,k = raw_input().split()
        a = int(a)
        b = int(b)
        k = int(k)  
        dictr = {}
        dictr[a] = k
        listy.append(dictr)
        dictr = {}
        dictr[b+1] = -k
        listy.append(dictr)
    #listy = listy.sort
    max_v = 0
    cur_v = 0
    for i in range(M*2):
        print listy
        
        #cur_v = cur_v + listy[i]
        max_v = max(max_v,cur_v)
    #print max_v
    
getmaximum()
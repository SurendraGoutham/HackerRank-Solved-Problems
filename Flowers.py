'''
Created on 25-Jul-2014

@author: 00003179
'''
#!/bin/python
# code snippet illustrating input/output methods 

N, K = raw_input().split()
N = int(N) #flowers
K = int(K) #friends
cost = 0
numbers = raw_input().split()
results = map(int, numbers)
results.sort(reverse=True)
loop = 1
for i in range (0,len(results)):
    if i%K == 0:
        loop = loop + 1
        #loop *
    else: cost = cost + results[i]
    

'''
Created on 27-Feb-2015

@author: 00003179
'''
N,M=[int(x) for x in raw_input().split()]
candies  = 0
for _ in range(M):
    a,b,k=[int(x) for x in raw_input().split()]
    candies  += (b-a+1)*k
print (candies/N)
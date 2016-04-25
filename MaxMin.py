'''
Created on 26-Feb-2015

@author: 00003179
'''
def getMin(candies):
    list1 = []
    for i in xrange(0,k):
        list1.append(candies[i])
    return max(list1) - min(list1)

n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
candies2 = []
for each in candies:
    if each not in candies2:
        candies2.append(each)

print getMin(candies2) 

    


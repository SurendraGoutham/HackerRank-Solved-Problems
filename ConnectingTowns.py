'''
Created on 10-Feb-2015

@author: 00003179
'''
def getCitiesCount(numbers):    
    product = 1
    for each in numbers:
        product *= each
    return product%1234567
    

T = input()
res = []
for i in range(T):    
    N = input()
    cities = raw_input().split()
    numbers = map(int, cities)
    res.append(getCitiesCount(numbers))
print '\n'.join(map(str, res))
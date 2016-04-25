<<<<<<< HEAD
'''
Created on 16-Feb-2015

@author: 00003179
'''

def getMaxSubArr(Arr):
    positiveSum = 0
    currentSum = bestSum = Arr[0]
    first =  Arr[0]
    for i in Arr[1:]:
        if i > 0:
            positiveSum = positiveSum + i        
        currentSum = max(0,currentSum + i)
        bestSum = max(currentSum,bestSum)
    if first > 0:        
        positiveSum = positiveSum + first
    if positiveSum == 0:
        positiveSum = max(Arr)
    if bestSum == 0:
        bestSum = max(Arr)
    positiveSum = max(positiveSum,bestSum)
        
    return str(bestSum) + " " + str(positiveSum)

T = input()
res = []
for each in xrange(T):
    N = input()
    nums = raw_input().split()
    numbers = map(int, nums)
    res.append(getMaxSubArr(numbers))
print '\n'.join(map(str, res))


=======
'''
Created on 16-Feb-2015

@author: 00003179
'''

def getMaxSubArr(Arr):
    positiveSum = 0
    currentSum = bestSum = Arr[0]
    first =  Arr[0]
    for i in Arr[1:]:
        if i > 0:
            positiveSum = positiveSum + i        
        currentSum = max(0,currentSum + i)
        bestSum = max(currentSum,bestSum)
    if first > 0:        
        positiveSum = positiveSum + first
    if positiveSum == 0:
        positiveSum = max(Arr)
    if bestSum == 0:
        bestSum = max(Arr)
    positiveSum = max(positiveSum,bestSum)
        
    return str(bestSum) + " " + str(positiveSum)

T = input()
res = []
for each in xrange(T):
    N = input()
    nums = raw_input().split()
    numbers = map(int, nums)
    res.append(getMaxSubArr(numbers))
print '\n'.join(map(str, res))


>>>>>>> origin/master

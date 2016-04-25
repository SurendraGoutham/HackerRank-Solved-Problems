'''
Created on 06-Jan-2015

@author: 00003179
'''

finalRes = []

def CutSticks(inputList):
    finalList = []
    leastnum = inputList[0]
    for each in inputList:
        res = each - leastnum
        if res > 0:
            finalList.append(res)
    flLen = len(finalList)
    if flLen > 0:
        finalRes.append(flLen)
        CutSticks(sorted(finalList))
        
if __name__ == '__main__':
    n = input()
    numbers = raw_input().split()
    results = map(int, numbers)
    finalRes.append(n)
    CutSticks(sorted(results))
    print '\n'.join(map(str, finalRes))

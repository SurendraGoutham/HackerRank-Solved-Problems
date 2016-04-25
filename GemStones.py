'''
Created on 30-Jul-2014

@author: 00003179
'''

import operator
from collections import OrderedDict

def gemStones(n,inputList):
    count,k = 0,0
    for each in inputList[0]:
        k = 1
        for j in xrange(1,len(inputList)):
            if each in inputList[j]:
                k += 1
            else:
                break
        if(k==(n)):
            count += 1
    return count
if __name__ == '__main__':
    n = input()
    inputDict = {}
    for i in range(0,n):
        inputStr = raw_input()
        inputDict[inputStr] = len(inputStr)
    sorted_dict = sorted(inputDict.iteritems(), key=operator.itemgetter(1))
    inList =[]
    for i in range(0,len(sorted_dict)):
        #To remove duplicate character in a string by maintaining the order of the String
        strk = "".join(OrderedDict.fromkeys(sorted_dict[i][0])) 
        inList.append(strk)
    print gemStones(n,inList)



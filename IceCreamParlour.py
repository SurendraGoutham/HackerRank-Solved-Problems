'''
Created on 23-Jul-2014

@author: 00003179
'''
# !/usr/bin/py

def icecreamparlour(m,n,costs):
    arrIndex = 0
    presIndex = 0
    temp = costs[0]
    while True:
        if m <= 0 or n <= 0 : return 0
        if (arrIndex+1) == len(costs):
            presIndex += 1
            temp = costs[presIndex]
            arrIndex = presIndex
        if (temp + costs[arrIndex+1]) == m:
            firstNumIndex = costs.index(temp)
            costs[costs.index(temp)] = 0
            print (firstNumIndex)+1 , (costs.index(costs[arrIndex+1]))+1
            break
            #return (firstNumIndex)+1,(costs.index(costs[arrIndex+1]))+1
        arrIndex += 1
            
if __name__ == '__main__':
    print "Test counts:"
    testCases = input()
    testNum = 1
    while testCases > 0:
        print "Test Case #" , testNum
        print "Type Total Money available:"
        m = input()
        print "Type Total flavours available:"
        n = input()
        print "Type flavours cost:"
        costs = map(int, raw_input().strip().split(" "))
        icecreamparlour(m,n,costs)
        testCases -= 1
        testNum += 1

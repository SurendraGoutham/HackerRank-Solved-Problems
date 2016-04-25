'''
Created on 01-Aug-2014

@author: 00003179
'''


def getPallindrome(inputStr):
    if (inputStr[::] == inputStr[::-1]):
        return True
    else: return False
        

inputStr = "abc"
if (getPallindrome(inputStr) != True):
    strlen = len(inputStr)
    k = strlen 
    for i in xrange(0,strlen):
        if (ord(inputStr[0]) != 97):
            diff =  ord(inputStr[0]) - 97
            op = diff
            inputStr[0] = 'a'
        print inputStr[i],inputStr[k-1]
        if inputStr[i] != inputStr[k-1]:
            k = k-1
else:
    print "count"
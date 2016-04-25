'''
Created on 01-Aug-2014

@author: 00003179
'''
def UtopianTree(inputList):
    for each in inputList:
        n = 1
        if each == 0:
            n = 1
        else:
            for j in xrange(1,each+1):
                if j % 2 == 0:
                    n = n + 1
                else:
                    n = 2 * n
        print n
        
if __name__ == '__main__':
    n = input()
    inputList =[]
    for i in range(0,n):
        inputNum = input()
        inputList.append(inputNum)
    UtopianTree(inputList)

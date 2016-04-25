'''
Created on 25-Jul-2014

@author: 00003179
'''

def findHackerRank(strg): 
    stringMatch = 'hackerrank';  
    for each in strg:
        listofWords = each.split()
        if listofWords[0] == stringMatch:
            if listofWords[len(listofWords)-1]== stringMatch:
                print 0
            else: print 1
        elif listofWords[len(listofWords)-1]== stringMatch:
            print 2
        else: print -1
        '''
        if each.startswith(stringMatch):
            if each.endswith(stringMatch):
                print 0
            else: print 1
        elif each.endswith(stringMatch):
                print 2
        else: print -1
        '''
if __name__ == '__main__':
    n = input()
    stg = []
    for i in range(0,n):
        inputStr = raw_input()
        stg.append(inputStr)
findHackerRank(stg)
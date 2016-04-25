'''
Created on 23-Feb-2015

@author: 00003179
'''
 
def findKbyBST(K,inputList):
    middleIndex = len(inputList)/2
    middleElement = inputList[middleIndex]
    if(middleElement == K):
        return "YES"
    if(middleElement > K):
        inputList = inputList[middleIndex:]
        print inputList
        findKbyBST(K,inputList)
    if(middleElement < K):
        inputList = inputList[:middleIndex]
        print inputList
        findKbyBST(K,inputList)
    return "NO"

M,N,K = map(int, raw_input().split())

for _ in xrange(M):
    for _ in xrange(N):        
        list_Of_Elements = []
        list_Of_Elements = map(int, raw_input().split())
        print findKbyBST(K,list_Of_Elements)
    
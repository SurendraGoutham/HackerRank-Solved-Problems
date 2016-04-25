'''
Created on 02-Dec-2014

@author: 00003179
'''
def insertionSort1(ar):
    v = ar[-1]
    arLen = len(ar)
    lastButOne = ar[arLen - 2]
    for each in ar:
        if each >= v: 
            return lastButOne

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort1(ar)

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i - 1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

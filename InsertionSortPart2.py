<<<<<<< HEAD
'''
Created on 01-Aug-2014

@author: 00003179
'''
def insertion_sort(ar):
    for i in xrange(1, len(ar)):
        j = i 
        key = ar[i]
        while key < ar[j-1] and (j > 0):
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = key
        print ' '.join(map(str, ar))
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
=======
'''
Created on 01-Aug-2014

@author: 00003179
'''
def insertion_sort(ar):
    for i in xrange(1, len(ar)):
        j = i 
        key = ar[i]
        while key < ar[j-1] and (j > 0):
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = key
        print ' '.join(map(str, ar))
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
>>>>>>> origin/master
insertion_sort(ar)
<<<<<<< HEAD
'''
Created on 01-Aug-2014

@author: 00003179
'''
def insertion_sort(count,ar):
    for i in xrange(1, len(ar)):
        j = i 
        key = ar[i]
        while key < ar[j-1] and (j > 0):
            ar[j] = ar[j-1]
            count += 1
            j -= 1
        ar[j] = key
    print count
        
m = input()
count = 0
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(count,ar)
#print " ".join(map(str,ar))
=======
'''
Created on 01-Aug-2014

@author: 00003179
'''
def insertion_sort(count,ar):
    for i in xrange(1, len(ar)):
        j = i 
        key = ar[i]
        while key < ar[j-1] and (j > 0):
            ar[j] = ar[j-1]
            count += 1
            j -= 1
        ar[j] = key
    print count
        
m = input()
count = 0
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(count,ar)
#print " ".join(map(str,ar))
>>>>>>> origin/master

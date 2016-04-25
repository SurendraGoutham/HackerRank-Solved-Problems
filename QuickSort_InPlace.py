'''
Created on 15-Apr-2015

@author: 00003179
'''
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        print more
        return less + pivotList + more
 
a = [1,3,9,8,2,7,5]
quickSort(a)


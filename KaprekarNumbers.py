<<<<<<< HEAD
'''
Created on 06-Apr-2015

@author: 00003179
'''
import math

def checkKaprekar(n):    
    a = 0
    temp = n
    k = n * n
    while (n > 0):
        a = a + 1
        n = n / 10  
    rem = k % int(math.pow(10, a))
    quo = k / int(math.pow(10, a))
    if ((rem + quo) == temp):
        return True 
    else:
        return False
   
p = int(input())
q = int(input())
res = []
for i in xrange(p,q+1):
    if(checkKaprekar(i)):
        res.append(i)

if res.__len__() == 0: print "INVALID RANGE"
=======
'''
Created on 06-Apr-2015

@author: 00003179
'''
import math

def checkKaprekar(n):    
    a = 0
    temp = n
    k = n * n
    while (n > 0):
        a = a + 1
        n = n / 10  
    rem = k % int(math.pow(10, a))
    quo = k / int(math.pow(10, a))
    if ((rem + quo) == temp):
        return True 
    else:
        return False
   
p = int(input())
q = int(input())
res = []
for i in xrange(p,q+1):
    if(checkKaprekar(i)):
        res.append(i)

if res.__len__() == 0: print "INVALID RANGE"
>>>>>>> origin/master
else: print ' '.join(map(str, res))
<<<<<<< HEAD
'''
Created on 08-Dec-2014

@author: 00003179
'''
'''
n = input()
m = input()
maxXOR = 0
for i in xrange(n,m+1):
    for k in xrange(m,n-1,-1):
        res = i ^ k
        if maxXOR <= res:
            maxXOR = res            
print maxXOR
'''


# Complete the function below.


def  maxXor( l,  r):
    maxXOR = 0
    for i in xrange(l,r+1):
        for k in xrange(r,l-1,-1):
            res = i ^ k
            if maxXOR <= res:
                maxXOR = res            
    return maxXOR

    

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
=======
'''
Created on 08-Dec-2014

@author: 00003179
'''
'''
n = input()
m = input()
maxXOR = 0
for i in xrange(n,m+1):
    for k in xrange(m,n-1,-1):
        res = i ^ k
        if maxXOR <= res:
            maxXOR = res            
print maxXOR
'''


# Complete the function below.


def  maxXor( l,  r):
    maxXOR = 0
    for i in xrange(l,r+1):
        for k in xrange(r,l-1,-1):
            res = i ^ k
            if maxXOR <= res:
                maxXOR = res            
    return maxXOR

    

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
>>>>>>> origin/master
print(res)
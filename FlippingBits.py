<<<<<<< HEAD
'''
Created on 02-Feb-2015

@author: 00003179
'''

T=input()
res = []

for _ in xrange(T):
    res.append(input()^(2**32 - 1))
=======
'''
Created on 02-Feb-2015

@author: 00003179
'''

T=input()
res = []

for _ in xrange(T):
    res.append(input()^(2**32 - 1))
>>>>>>> origin/master
print '\n'.join(map(str, res))
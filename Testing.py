'''
Created on 28-Nov-2014

@author: 00003179
'''
#print range(2,10,4)

#print 23123234/1000
#print 1233454%100

number = 123416866
firstPart = number / 10000
secondPart = number - firstPart * 10000

#print firstPart, secondPart

import string

s = "string. With. Punctuation"
table = string.maketrans("","")

def test_trans(s):
    return s.translate(table, string.punctuation)

#print test_trans(s)

#print list(s)

n = 378
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1
    print (n)
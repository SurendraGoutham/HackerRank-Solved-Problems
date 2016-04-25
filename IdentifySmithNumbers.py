'''
Created on 07-Apr-2015

@author: 00003179
'''
from math import floor, sqrt

def sum_digits(n): # faster approach to calculate the sum of digits in a number
    r = 0
    if N < 11:
        return n
    while n:
        r, n = r + n % 10, n / 10
    return r
def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]
 
if __name__ == '__main__':
    N = int(input())
    primeFactorsSum = 0 
    inputDigitsSum = sum_digits(N)
    k = fac(N)
    for each in k:
        primeFactorsSum = primeFactorsSum + sum_digits(each)
    if N == 1: print 0
    else: print(1 if primeFactorsSum == inputDigitsSum else 0)

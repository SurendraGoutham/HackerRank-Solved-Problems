'''
Created on 06-Apr-2015

@author: 00003179
'''
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
 
def multiple_gcd(numbers):
    return reduce(lambda x, y: gcd(x, y), numbers)

if __name__ == '__main__':
    res = []
    t = input()
    for _ in xrange(t):
        n = input()
        values = map(int, raw_input().split())
        if len(values) < 2:
            res.append("NO")
            continue
        if (multiple_gcd(values) == 1):
            res.append("YES")
        else:
            res.append("NO")
            
print '\n'.join(map(str, res))

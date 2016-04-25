'''
Created on 30-Jul-2014

@author: 00003179
'''
def lastStone(a, b, n):
    if a == b:
        return [a * (n - 1)]
    if a < b:
        return lastStone(b, a, n)
    return [i * a + (n - i - 1) * b for i in range(n)]

T = int(input())
res = []
for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    list1 = lastStone(a, b, n)
    str1 = ' '.join(str(e) for e in list1)
    res.append(str1)
print '\n'.join(map(str, res))
    
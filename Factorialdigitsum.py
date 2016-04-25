import math
m = input()
res = []
for i in range(m):
    inputnum = input()
    res.append(sum(map(int, str(math.factorial(inputnum)))))
print '\n'.join(map(str, res))



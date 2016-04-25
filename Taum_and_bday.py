<<<<<<< HEAD
'''
Created on 05-Mar-2015

@author: 00003179
'''

def getMinimal(X,Y,Z,B,W):
    mini = min(X,Y)
    if mini == X:
        if X+Z < Y: return (B+W)*X + (W*Z)
        else: return (B)*X + (W)*Y
    if mini == Y:
        if Y+Z < X: return (B+W)*Y + (B*Z)
        else: return (B)*X + (W)*Y

T = input()
res = []
for _ in xrange(T):
    B,W = raw_input().split()
    X,Y,Z = raw_input().split()
    res.append(getMinimal(int(X),int(Y),int(Z),int(B),int(W)))

=======
'''
Created on 05-Mar-2015

@author: 00003179
'''

def getMinimal(X,Y,Z,B,W):
    mini = min(X,Y)
    if mini == X:
        if X+Z < Y: return (B+W)*X + (W*Z)
        else: return (B)*X + (W)*Y
    if mini == Y:
        if Y+Z < X: return (B+W)*Y + (B*Z)
        else: return (B)*X + (W)*Y

T = input()
res = []
for _ in xrange(T):
    B,W = raw_input().split()
    X,Y,Z = raw_input().split()
    res.append(getMinimal(int(X),int(Y),int(Z),int(B),int(W)))

>>>>>>> origin/master
print '\n'.join(map(str, res))
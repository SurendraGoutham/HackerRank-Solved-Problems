'''
Created on 11-Feb-2015

@author: 00003179
'''

def getAlternate(strg):    
        length = len(strg)
        count = answer = 0
        for i in xrange(0,length):
            if (i == 0 or strg[i] == strg[i-1]):
                count += 1
            else:
                if(count > 1):
                    k = count - 1
                    answer += k
                count =1
        if (count > 1):
            k = count - 1
            answer += k
        return answer

T = input()
res = []
for _ in xrange(T):
    strg = raw_input()
    res.append(getAlternate(strg))
print '\n'.join(map(str, res))
    

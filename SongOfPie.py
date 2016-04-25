'''
Created on 06-Apr-2015

@author: 00003179
'''

import string

table = string.maketrans("","")

def test_trans(s):
    return s.translate(table, string.punctuation)

def retPie(strg):
    strg = test_trans(strg)
    PieV = ""
    words = strg.split()
    for each in words:
        PieV = PieV + "" + str(len(each))
    return PieV

T = int(input())
pie = "31415926535897932384626433833"
res = []
for _ in range(T):
    strg = raw_input()
    inPie = retPie(strg)
    k = len(inPie)
    orgPie = pie[:k]
    if(inPie == orgPie): res.append("It's a pi song.")
    else: res.append("It's not a pi song.")

print '\n'.join(map(str, res))    
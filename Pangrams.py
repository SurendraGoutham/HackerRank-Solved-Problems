'''
Created on 27-Nov-2014

@author: 00003179
'''

import string
#print list(map(chr, range(97, 123)))
#print list(string.ascii_lowercase)


def panagrams(inputStr):
    if len(inputStr) >= 26:
        alphaList = list(string.ascii_lowercase)
        panaList = []
        for each in inputStr:
            if each in alphaList:
                alphaList.remove(each)
                panaList.append(each)
                if len(panaList) == 26:
                    return 'pangram'
    return 'not pangram'

if __name__ == '__main__':
    inputStr = raw_input().replace(" ", "").lower()
    print panagrams(inputStr)

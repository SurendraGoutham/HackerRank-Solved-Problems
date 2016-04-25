<<<<<<< HEAD
'''
Created on 23-Jul-2014

@author: 00003179
'''
# !/usr/bin/py

def lonelyinteger(b):
    fullwordcount = {}
    # finalList =[]
    for i in range(0, len(b)):
        if b[i] not in fullwordcount:
            fullwordcount[b[i]] = 1
        else:
            fullwordcount[b[i]] += 1 
    if 1 in fullwordcount.values():
        for key, value in fullwordcount.iteritems():
            if value == 1:
                return key
                # finalList.append(key)
    else:
        return "No Lone Integer"
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

'''
#submitted

def lonelyinteger(b):
    fullwordcount = {}
    for i in range(0,len(b)):
        if b[i] not in fullwordcount:
            fullwordcount[b[i]] = 1
        else:
            fullwordcount[b[i]] += 1 
    if 1 in fullwordcount.values():
        for key,value in fullwordcount.iteritems():
            if value == 1:
                return key
    else:
        return "No Lone Integer"
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

'''

=======
'''
Created on 23-Jul-2014

@author: 00003179
'''
# !/usr/bin/py

def lonelyinteger(b):
    fullwordcount = {}
    # finalList =[]
    for i in range(0, len(b)):
        if b[i] not in fullwordcount:
            fullwordcount[b[i]] = 1
        else:
            fullwordcount[b[i]] += 1 
    if 1 in fullwordcount.values():
        for key, value in fullwordcount.iteritems():
            if value == 1:
                return key
                # finalList.append(key)
    else:
        return "No Lone Integer"
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

'''
#submitted

def lonelyinteger(b):
    fullwordcount = {}
    for i in range(0,len(b)):
        if b[i] not in fullwordcount:
            fullwordcount[b[i]] = 1
        else:
            fullwordcount[b[i]] += 1 
    if 1 in fullwordcount.values():
        for key,value in fullwordcount.iteritems():
            if value == 1:
                return key
    else:
        return "No Lone Integer"
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

'''

>>>>>>> origin/master

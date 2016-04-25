<<<<<<< HEAD
'''
Created on 26-Nov-2014

@author: 00003179
'''
def findtheDigits(num):
    count = 0
    for each in num:
        if int(each) != 0:
            if int(num) % int(each) == 0:
                count = count + 1
    return count 

if __name__ == '__main__':
    n = input()
    listy = []
    for i in range(0,n):
        num = raw_input()
        listy.append(findtheDigits(num))
    for each in listy:
        print each
=======
'''
Created on 26-Nov-2014

@author: 00003179
'''
def findtheDigits(num):
    count = 0
    for each in num:
        if int(each) != 0:
            if int(num) % int(each) == 0:
                count = count + 1
    return count 

if __name__ == '__main__':
    n = input()
    listy = []
    for i in range(0,n):
        num = raw_input()
        listy.append(findtheDigits(num))
    for each in listy:
        print each
>>>>>>> origin/master

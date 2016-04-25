<<<<<<< HEAD
'''
Created on 26-Nov-2014

@author: 00003179
'''
import math

sqrtValue = math.sqrt(5)

getFibo = lambda n: int(((1+sqrtValue)**n-(1-sqrtValue)**n) / ((2**n)*sqrtValue))

def isFibo(n):
    fibList = [0,1,2,3,5,8]
    if n not in fibList:
        if(n % 2 == 0):
            for i in range(3,n+1,3):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        elif(n % 3 == 0):
            for i in range(4,n+1,4):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        elif(n % 5 == 0):
            for i in range(5,n+1,5):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        return 'IsNotFibo'
    else: return 'IsFibo'


if __name__ == '__main__':
    n = input()
    listy = []
    for i in range(0,n):
        num = raw_input()
        listy.append(isFibo(int(num)))
    for each in listy:
=======
'''
Created on 26-Nov-2014

@author: 00003179
'''
import math

sqrtValue = math.sqrt(5)

getFibo = lambda n: int(((1+sqrtValue)**n-(1-sqrtValue)**n) / ((2**n)*sqrtValue))

def isFibo(n):
    fibList = [0,1,2,3,5,8]
    if n not in fibList:
        if(n % 2 == 0):
            for i in range(3,n+1,3):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        elif(n % 3 == 0):
            for i in range(4,n+1,4):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        elif(n % 5 == 0):
            for i in range(5,n+1,5):
                fibVal = getFibo(i)
                if fibVal <= n:
                    if fibVal == n:
                        return 'IsFibo'
                else: return 'IsNotFibo'
        return 'IsNotFibo'
    else: return 'IsFibo'


if __name__ == '__main__':
    n = input()
    listy = []
    for i in range(0,n):
        num = raw_input()
        listy.append(isFibo(int(num)))
    for each in listy:
>>>>>>> origin/master
        print each
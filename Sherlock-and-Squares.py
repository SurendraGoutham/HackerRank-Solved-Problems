<<<<<<< HEAD
'''
Created on 06-Apr-2015

@author: 00003179
'''
import math


def squares_between(a, b):
    print a , b    
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt((a - 1)))
    return count


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a = map(int, raw_input().strip().split(" "))
        b = map(int, raw_input().strip().split(" "))
        #a, b = tuple(int(pair) for pair in input().split())
=======
'''
Created on 06-Apr-2015

@author: 00003179
'''
import math


def squares_between(a, b):
    print a , b    
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt((a - 1)))
    return count


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a = map(int, raw_input().strip().split(" "))
        b = map(int, raw_input().strip().split(" "))
        #a, b = tuple(int(pair) for pair in input().split())
>>>>>>> origin/master
        print(squares_between(a, b))
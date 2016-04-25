'''
Created on 30-Jul-2014

@author: 00003179
'''

def getMedian(n,nums):
    return sorted(nums)[n//2]

if __name__ == '__main__':
    n = input()
    nums = map(int, raw_input().strip().split(" "))
    print getMedian(n,nums)

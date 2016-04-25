'''
Created on 27-Feb-2015

@author: 00003179
'''
'''
import itertools

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else: return False
    
found = False
perms = [''.join(p) for p in itertools.permutations(string)]
perms = list(set(perms))

for each in perms:
    if isPalindrome(each):
        found = True
        break
    
if not found:
    print("NO")
else:
    print("YES")

'''
from collections import Counter


def isPalindrome(string):
    # Observation: one letter can appear odd number of times in a palindrome.
    # The rest must appear an even number of times.
    letter_counts = Counter(string).values()
    odd_counts = [count for count in letter_counts if count % 2 != 0]
    print odd_counts
    return len(odd_counts) <= 1


if __name__ == '__main__':
    string = raw_input()
    print('YES' if isPalindrome(string) else 'NO')
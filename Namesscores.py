<<<<<<< HEAD
'''
Created on 01-Aug-2014

@author: 00003179
'''
import string

n = input()
names = (open('names.txt','r')).read()
names = names.replace('"','')
names = names.split(",")
names = sorted(names)

totalScore = 0

for eachname in names: #Taking each name in all the names
    nameValue = 0
    for eachletter in eachname: #Taking each letter in eachname
        nameValue += string.ascii_uppercase.index(eachletter) + 1 #this will give the index of an alphabet, using string library                 
    totalScore += (names.index(eachname) + 1) * nameValue # Counting score position * namevalue 
print totalScore
=======
'''
Created on 01-Aug-2014

@author: 00003179
'''
import string

n = input()
names = (open('names.txt','r')).read()
names = names.replace('"','')
names = names.split(",")
names = sorted(names)

totalScore = 0

for eachname in names: #Taking each name in all the names
    nameValue = 0
    for eachletter in eachname: #Taking each letter in eachname
        nameValue += string.ascii_uppercase.index(eachletter) + 1 #this will give the index of an alphabet, using string library                 
    totalScore += (names.index(eachname) + 1) * nameValue # Counting score position * namevalue 
print totalScore
>>>>>>> origin/master

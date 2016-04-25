'''
Created on 25-Jul-2014

@author: 00003179
'''
import math

def encryption(strg):
    strg = strg.replace(' ','')
    strLength = len(strg)
    rows = int(math.floor(math.sqrt(strLength)))
    columns = int(math.ceil(math.sqrt(strLength)))
    prod = rows*columns
    count =1 
    if prod >= strLength:
        count +=1
    else:
        while(prod <= strLength):
            rows = rows + 1
            prod = rows*columns
    k = 0 
    matrix = [["" for i in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if(k < strLength):
                matrix[i][j] = strg[k]
            k += 1
    newStr =''
    for i in range(columns):
        for j in range(rows):
            newStr = newStr + matrix[j][i]
        newStr = newStr + ' '
    print newStr

if __name__ == '__main__':
    inputStr = raw_input()
    encryption(inputStr)
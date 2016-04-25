'''
Created on 10-Apr-2015

@author: 00003179
'''
def check_all(arr_list):
    main_count = 0
    for each_list in lists:
        temp = set(each_list)
        if temp.__len__() == 1:
            temp2 = set(arr_list)
            if temp2 == temp:
                main_count = main_count + 1
        else:
            count_x = 0
            for item in arr_list:
                if item in temp:
                    count_x = count_x + 1
                    temp.remove(item)
                    if count_x == len(arr_list):
                        main_count = main_count + 1
                        break
    return main_count

def check_any(arr_list):
    main_count = 0
    for each_list in lists:
        temp = set(each_list)
        for item in arr_list:
            if item in temp:
                main_count = main_count + 1
                break
    return main_count

def check_some(arr_list):
    main_count = arrs
    for each_list in lists:
        temp = set(each_list)
        count_x = 0
        for item in arr_list:
            if item in temp:
                count_x = count_x + 1
                temp.remove(item)
                if count_x == len(arr_list):
                    main_count = main_count - 1
        if count_x == 0:
            main_count = main_count - 1
    return main_count
    

arrs = int(input())
lists = []
for i in xrange(arrs):
    K = raw_input().split()
    arr_list = []
    for each in K[1:]:
        arr_list.append(each)
    lists.append(arr_list)

T = int(input())
res = []
for i in xrange(T):
    K = raw_input().split()
    check_no = int(K[0])
    if check_no == 1:
        val = check_all(K[2:])
        res.append(val)
    elif check_no == 2:
        val = check_any(K[2:])
        res.append(val)
    else: 
        val = check_some(K[2:])
        res.append(val)

print '\n'.join(map(str, res))

        
    
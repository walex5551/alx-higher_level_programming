#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    add = 0
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
            add += i
    return add

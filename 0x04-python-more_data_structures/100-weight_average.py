#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = sum([num[0] * num[1] for num in my_list])
    result = n / sum([num[1] for num in my_list])
    return result

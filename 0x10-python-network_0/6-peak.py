#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """

    hi = len(list_of_integers)
    if hi == 0:
        return None
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)

    mid = hi // 2

    peak = list_of_integers[mid]
    left = list_of_integers[mid - 1]
    right = list_of_integers[mid + 1]

    if peak > left and peak > right:
        return peak
    elif peak < left:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])

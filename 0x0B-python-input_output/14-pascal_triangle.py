#!/usr/bin/python3
"""
14-pascal_triangle : 1 function

"""


def pascal_triangle(n):
    """ Return list of lists of a pascal triangle in range n

        Args:
            n (obj : 'int') : size of triangle
    """
    """
    if n <= 0:
        return []

    tri = [[] for i in range(n)]

    tri[0] = 1
    for i in range(n):
        tri[i][0] = 1
        for j in range(i + 1):
            if j < len(tri[i - 1]):
                tri[i].append(tri[i - 1][j - 1] + tri[i - 1][j])

    return tri
    """
    if n <= 0:
        return []

    tri = [[0 for x in range(i + 1)] for i in range(n)]

    for i in range(n):
        tri[i][0] = 1
        for j in range(1, i + 1):
            if j < len(tri[i - 1]):
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
            else:
                tri[i][j] = 1
    return tri

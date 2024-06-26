"""
https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
"""

import numpy

n, m, _ = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((arr1, arr2)))
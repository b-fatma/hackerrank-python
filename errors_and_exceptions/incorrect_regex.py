"""
https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
"""
# works only using PyPy3
import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except re.error:
        print("False")



"""
https://www.hackerrank.com/challenges/python-mod-divmod?isFullScreen=true
"""

a, b = [int(input()) for _ in range(2)]
print(a//b, a%b, divmod(a, b), sep='\n')
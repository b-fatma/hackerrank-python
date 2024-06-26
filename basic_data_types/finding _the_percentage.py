"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = 0
    for x in student_marks[query_name]:
        avg += x
    print("{:.2f}".format(avg/3))
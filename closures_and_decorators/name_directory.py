"""
https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
"""

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: int(x[2])) 
        return map(f, people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
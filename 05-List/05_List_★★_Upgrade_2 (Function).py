def index_of(grades, ID):
    mark = 0
    for item in grades:
        if item[0] == ID:
            x = grades.index(item)
            mark = 1
            return x
    if mark == 0:
        return -1    
def upgrade(grades, IDs):
    for item in grades:
        for num in IDs:
            if num == item[0]:
                if item[1] == 'A':
                    break
                else:
                    item[1] = NumToAlphabet(AlphabetToNum(item[1])+1)
    grades.sort()

def AlphabetToNum(x):
    if x == 'A':
        return 8
    if x == 'B+':
        return 7
    if x == 'B':
        return 6
    if x == 'C+':
        return 5
    if x == 'C':
        return 4
    if x == 'D+':
        return 3
    if x == 'D':
        return 2
    if x == 'F':
        return 1
def NumToAlphabet(x):
    if x == 8:
        return 'A'
    if x == 7:
        return 'B+'
    if x == 6:
        return 'B'
    if x == 5:
        return 'C+'
    if x == 4:
        return 'C'
    if x == 3:
        return 'D+'
    if x == 2:
        return 'D'
    if x == 1:
        return 'F'
exec(input())
exec(input())
exec(input())

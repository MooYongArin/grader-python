NickNameFirst,MonthFirst,DateFirst,YearFirst = input().split()
NickNameSecond,MonthSecond,DateSecond,YearSecond = input().split()

def MonthToNumber(x):
    if x == 'January':
        return 1
    if x == 'February':
        return 2
    if x == 'March':
        return 3
    if x == 'April':
        return 4
    if x == 'May':
        return 5
    if x == 'June':
        return 6
    if x == 'July':
        return 7
    if x == 'August':
        return 8
    if x == 'September':
        return 9
    if x == 'October':
        return 10
    if x == 'November':
        return 11
    if x == 'December':
        return 12

if YearFirst > YearSecond:
    print(NickNameSecond)
elif YearSecond > YearFirst:
    print(NickNameFirst)
elif YearSecond == YearFirst:
    if MonthToNumber(MonthFirst) > MonthToNumber(MonthSecond):
        print(NickNameSecond)
    elif MonthToNumber(MonthSecond) > MonthToNumber(MonthFirst):
        print(NickNameFirst)
    elif MonthToNumber(MonthFirst) == MonthToNumber(MonthSecond):
        if DateFirst < DateSecond:
            print(NickNameSecond)
        elif DateFirst > DateSecond:
            print(NickNameFirst)
        elif DateFirst == DateSecond:
            print(NickNameFirst, NickNameSecond)

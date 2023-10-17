def is_odd(n):
    if n%2==0:
        return False
    return True
def has_odds(x):
    for item in x:
        if is_odd(item):
            return True
    return False
def all_odds(x):
    for item in x:
        if not is_odd(item):
            return False
    return True
def no_odds(x):
    check = True
    for item in x:
        if is_odd(item):
            check = False
    return check
def get_odds(x):
    lst=[]
    for item in x:
        if is_odd(item):
            lst.append(item)
    return lst
def zip_odds(a, b):
    lst = []
    lsta = get_odds(a)
    lstb = get_odds(b)
    if len(lsta)>=len(lstb):
        for i in range(len(lsta)):
            lst += [lsta[i]]
            if i<len(lstb):
                lst += [lstb[i]]
    else:
        for i in range(len(lstb)):
            if i<len(lsta):
                lst += [lsta[i]]
            lst += [lstb[i]]
    return lst

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ

def make_int_list(x):
    lst = []
    x = x.split()
    for item in x:
        lst.append(int(item))
    return lst
def is_odd(e):
    if e%2 == 0:
        return False
    else:
        return True
def odd_list(alist):
    lst = []
    for item in alist:
        if is_odd(item):
            lst.append(item)
    return lst
def sum_square(alist):
    _sum = 0
    for item in alist:
        _sum += int(item)**2
    return _sum
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader

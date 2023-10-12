def missing_digits(t):
    test = '0123456789'
    lst = []
    for item in test:
        if item not in t:
            lst.append(int(item))
    return lst
exec(input()) # DON'T remove this line
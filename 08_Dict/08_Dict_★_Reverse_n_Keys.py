def reverse(d):
    reverse_d = {}
    for item in d:
        reverse_d[d[item]] = item
    return reverse_d

def keys(d, v):
    lst = []
    for item in d:
        if d[item] == v:
            lst.append(item)
    return lst

exec(input().strip())

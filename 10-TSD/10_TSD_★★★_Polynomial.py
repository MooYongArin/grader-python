def add_poly(p1, p2):
    dct = dict([(x,y) for y,x in p2])
    for a,b in p1:
        if b in dct:
            dct[b] += a
        else:
            dct[b] = a
    return [(dct[e],e) for e in sorted(dct)[::-1] if dct[e] != 0]
def mult_poly(p1, p2):
    dct = {}
    for a,b in p1:
        for c,d in p2:
            y = b+d
            x = a*c
            if y in dct:
                dct[y] += x
            else:
                dct[y] = x
    return [(dct[e],e) for e in sorted(dct)[::-1] if dct[e] != 0]
for i in range(3):
 exec(input().strip())
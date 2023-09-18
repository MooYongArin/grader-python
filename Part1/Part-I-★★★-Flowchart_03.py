import math
a,b,c,d = [int(x) for x in input().split()]

if a == 1:
    tempc = c
    tempd = d
    c = tempd
    d = tempc
    if b == 1:
        c +=  d
    else:
        if b == 2:
            c -= d
        else:
            if b != 3:
                c = c + c**d
            else:
                c = c/d
    a = (d+(((c/b)**3) + d)**0.5)/(2 + (b*d))
else:
    if a == 2:
        if b > 1:
            c += d
        if b > 2:
            c = c/d
        if b > 3:
            c = c + c**d
        else:
            a = math.log(c,10)
    else:
        while a > d:
            a -= 2
            if a < b:
                break
            else:
                c += a
print(a,b,c,d)
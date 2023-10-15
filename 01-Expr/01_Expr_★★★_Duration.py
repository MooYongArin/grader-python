h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

if s2>=s1:
    sa = s2-s1
    if m2>=m1:
        ma = m2-m1
        ha = h2-h1
    else:
        ma = m2-m1+60
        ha = h2-h1-1
else:
    sa = s2-s1+60
    m2 -= 1
    if m2>=m1:
        ma = m2-m1
        ha = h2-h1
    else:
        ma = m2-m1+60
        ha = h2-h1-1
        
print(str(ha%24)+":"+str(ma%60)+":"+str(sa%60))
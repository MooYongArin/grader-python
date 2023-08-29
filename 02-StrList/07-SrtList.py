n = int(input())
x1 = (n//(10**28))%10
x2 = n//(10**21)%10
x3 = n//(10**14)%10
x4 = n//(10**7)%10
x5 = n%10

y1 = (n//(10**24))%10
y2 = n//(10**19)%10
y3 = n//(10**14)%10
y4 = n//(10**9)%10
y5 = n//(10**4)%10

x = str(x1)+str(x2)+str(x3)+str(x4)+str(x5)
y = str(y1)+str(y2)+str(y3)+str(y4)+str(y5)
z = int(x) + int(y) + 10000

z1 = (z//1000)%10
z2 = (z//100)%10
z3 = (z//10)%10

al = z1 + z2 + z3
code1 = str(z1) + str(z2) + str(z3)
al1 = al%10
al2 = al1+1
def NumToAl(x):
    if x == 1:
        return 'A'
    if x == 2:
        return 'B'
    if x == 3:
        return 'C'
    if x == 4:
        return 'D'
    if x == 5:
        return 'E'
    if x == 6:
        return 'F'
    if x == 7:
        return 'G'
    if x == 8:
        return 'H'
    if x == 9:
        return 'I'
    if x == 10:
        return 'J'
print(code1 + NumToAl(al2))
import math

a,b,c = input().split(",")
y = int(b + c) - int("0" + b)
d = ""
for i in range(len(c)):
    d = d + '9'
for i in range(len(b)):
    d = d + '0'

ans_top = ((int(d)*int(a))+y)
ans_bottom = int(d)
ans = math.gcd(ans_top,ans_bottom)
print(ans)
ans_top_new = int(ans_top//ans)
ans_bottom_new = int(ans_bottom//ans)
print(ans_top_new ," / ", ans_bottom_new )

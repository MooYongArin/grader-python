par = int()
stroke = int()
choose = int()
fix_stroke = int()
sum_stroke = 0
sum_fix_stroke = 0
sum_par = 0

def floor(x):
    if x >= 0:
        x = int(x)
    else:
        x -= 1
        x = int(x)
    return x

for i in range(9):
    par,stroke,choose = input().split()
    if choose == '1':
        if int(par) + 2 >= int(stroke):
            fix_stroke = int(stroke)
        else:
            fix_stroke = int(par) + 2
    else:
        fix_stroke = 0
    sum_fix_stroke += fix_stroke
    sum_par += int(par)
    sum_stroke += int(stroke)
sum_fix_stroke = sum_fix_stroke * 1.5
sum_fix_stroke = sum_fix_stroke - sum_par
sum_fix_stroke = sum_fix_stroke * 0.8
handicap = floor(sum_fix_stroke)
net_score = sum_stroke - handicap

print(sum_stroke)
print(handicap)
print(net_score)
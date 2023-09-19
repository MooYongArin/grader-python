ans = input()
stu = input()

if len(ans) != len(stu):
    print('Incomplete answer')
else:
    sc = 0
    for i in range(len(ans)):
        if ans[i] == stu[i]:
            sc += 1
    print(sc)


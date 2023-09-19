_sum = 0
n = 0
while True:
    x = input()
    if x != 'q':
        _sum += float(x)
        n += 1
    else:
        break
if n!=0:
    avg = _sum/n
    print(round(avg,2))
else:
    print('No Data')
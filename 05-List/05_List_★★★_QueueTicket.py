q = list() # ลิสต์ q ใช้เก็บข้อมูลบัตรคิวที่เหมาะสม
n = int(input()) 
time = []
_sum = 0
i=0
amount = 0
for k in range(n):
    c = input().split() # อ่านข้อมูลค าสั่ง
    if c[0] == 'reset':
        x = int(c[1])
    elif c[0] == 'new':
        print('ticket',x)
        time.append([x,c[1]])
        time.sort()
        x+=1
    elif c[0] == 'next':
        print('call',time[i][0])
        i+=1
    elif c[0] == 'order':
        for item in time:
            if item[0] == time[i-1][0]:
                current = item[0]
                number = item[1]
        delta = int(c[1]) - int(number)
        _sum += delta
        amount += 1
        print('qtime',current,delta)
    elif c[0] == 'avg_qtime':
        print( 'avg_qtime',round(_sum/amount,4) )
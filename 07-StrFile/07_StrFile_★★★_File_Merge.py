def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", "" 

filename,filename_2 = input().split()

f_1 = open(filename)
f_2 = open(filename_2)
start1,gra1 = read_next(f_1)
start2,gra2 = read_next(f_2)

while start1 != '' and start2 != '':
    if start1[8:] < start2[8:] or (start1[8:] == start2[8:] and start1 < start2):
        print(start1,gra1)
        start1,gra1 = read_next(f_1)
    else:
        print(start2,gra2)
        start2,gra2 = read_next(f_2)

while start1 != '':
    print(start1,gra1)
    start1,gra1 = read_next(f_1)

while start2 != '':
    print(start2,gra2)
    start2,gra2 = read_next(f_2)

f_1.close()
f_2.close()
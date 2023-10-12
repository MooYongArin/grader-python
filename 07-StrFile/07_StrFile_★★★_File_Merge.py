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
print(f_1.readline())


# print(read_next(f_1))
# print(read_next(f_2))
# keep = ""
# while True:
#     if keep == read_next(f_1)[0][8:]:
#         print(read_next(f_1))
#         keep = read_next(f_1)[0][8:]
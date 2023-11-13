fname = input().strip()
f = open(fname)
data = f.read()
word = ''
lst = []
for alpha in data:
    if alpha != '.': 
        word += alpha
    else:
        if word != '':
            lst.append(word)
        word = ''
print(lst)
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1) # เพิ่มรอบละ 9 ขีด ตามด้วยตัวเลข
ruler += '-'*(k%10) # เพิ่มที่เหลือ (ถ้ามี)
print(ruler)
total = 0
line = ''
while total < k:
    line += data[total]
    total += 1
print(line)
f.close()
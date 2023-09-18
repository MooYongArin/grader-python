Text_STR = input()
Text_STR += " "
str2RLE_ans = ""
count = 0
for i in range(1,len(Text_STR)):
    count += 1
    if Text_STR[i] != Text_STR[i-1]:
        str2RLE_ans += str(Text_STR[i-1]) + " " + str(count) + " "
        count = 0
print(str2RLE_ans)
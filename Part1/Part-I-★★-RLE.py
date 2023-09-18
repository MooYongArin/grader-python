Type = input().strip()

if Type == 'str2RLE':
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
elif Type == 'RLE2str':
    text_RLE = input().split()
    RLE2str_ans = ""
    for i in range(len(text_RLE)):
        if i % 2 == 0:
            RLE2str_ans += text_RLE[i]*int(text_RLE[i+1])
    print(RLE2str_ans)
else :
    print("Error")
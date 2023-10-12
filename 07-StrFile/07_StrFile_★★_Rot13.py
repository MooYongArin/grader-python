upper_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_text = upper_text.lower()
all_ans = []
while True:
    se = input()
    if se == 'end':
        break
    ans = ""
    for item in se:
        if 'a'<=item<='z':
            index = lower_text.find(item)
            if index >= 13:
                ans += lower_text[index-13]
            else:
                ans += lower_text[index+13]
        elif 'A'<=item<='Z':
            index = upper_text.find(item)
            if index >= 13:
                ans += upper_text[index-13]
            else:
                ans += upper_text[index+13]
        else:
            ans += item
    all_ans.append(ans)
for item in all_ans:
    print(item)
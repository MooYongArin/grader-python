sentence = input()
strip_text = ""

for item in sentence:
    item = item.lower()
    if '0'<=item<='9' or 'a'<=item<='z':
        strip_text += item
    else:
        strip_text += " "
strip_text = strip_text.split()
ans = ""
for i in range(len(strip_text)):
    if i != 0:
        ans += strip_text[i][0].upper() + strip_text[i][1:]
    else:
        ans += strip_text[i]
print(ans)
text = input().lower()
check = input().lower()

text_keep = []
for item in text:
    if 'a'<=item<='z' or '0'<=item<='9':
        text_keep.append(item)
check_keep = []
for item in check:
    if 'a'<=item<='z' or '0'<=item<='9':
        check_keep.append(item)

check = True
if len(text_keep) != len(check_keep):
    check = False
text_keep.sort()
check_keep.sort()
if check:
    for i in range(len(text_keep)):
        if text_keep[i]!= check_keep[i]:
            check = False
            break
if check:
    print("YES")
else:
    print("NO")
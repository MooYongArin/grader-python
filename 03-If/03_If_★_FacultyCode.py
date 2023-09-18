x = input()
mark = 0
save = ['01','02','51','53','55','58']
for i in range(21):
    save.append(str(20+i))
for item in save:
    if x == item:
        print('OK')
        mark = 1

if mark == 0:
    print('Error')
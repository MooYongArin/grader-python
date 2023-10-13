import math
def MonthToDay(x,y):
    _bc = y - 543
    if x == 1:
        return 31
    if x == 2:
        if (_bc%4 == 0 and _bc%100!=0) or (_bc%4 == 0 and _bc%100==0 and _bc%400==0):
            return 29
        else:
            return 28
    if x == 3:
        return 31
    if x == 4:
        return 30
    if x == 5:
        return 31
    if x == 6:
        return 30
    if x == 7:
        return 31
    if x == 8:
        return 31
    if x == 9:
        return 30
    if x == 10:
        return 31
    if x == 11:
        return 30
    if x == 12:
        return 31

bd, bm, by, d, m, y = [int(e) for e in input().split()]

dy = y - by
# รวมวันจากปี
sum_day = (dy-1)*365
# รวมวันจากเดือน
for i in range(1,m):
    sum_day += MonthToDay(i,y)
for j in range(12,bm,-1):
    sum_day += MonthToDay(j,by)

# รวมเศษวัน
sum_day += d-1
sum_day += MonthToDay(bm,by) - bd + 1
phy = math.sin((2*math.pi*sum_day)/23)
emo = math.sin((2*math.pi*sum_day)/28)
intel = math.sin((2*math.pi*sum_day)/33)
print( "{} {:.2f} {:.2f} {:.2f}".format(sum_day,phy,emo,intel) ) 
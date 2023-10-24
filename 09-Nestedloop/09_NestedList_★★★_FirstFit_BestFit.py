def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for item in L:
        if e + sum(item) <= 100:
            item.append(e)
            return
    L.append([e]) # ใส่ไม่ได้เลย
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    test = [] 
    for item in L:
        if e + sum(item) <= 100:
            test.append(100 - (e + sum(item)))
        else:
            test.append(100)
    if test == []:
        L.append([e])
        return
    _min = min(test)
    if _min == 100:
        L.append([e])
    else:
        L[test.index(_min)].append(e)

def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    lst = []
    for item in D:
        first_fit(lst,item)
    return lst
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    lst = [[D[0]]]
    for item in D[1:]:
        best_fit(lst,item)
    return lst
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
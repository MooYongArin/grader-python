def read_date(): # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
    dct = {'Jan':1,}
    mname = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    x = input().split()
    x[0] = int(x[0])
    x[1] = mname.index(x[1])+1
    x[2] = int(x[2])
    return x
def zodiac(d1,m1): # คืนชื่อราศีของวัน d เดือน m
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1
def days_in_feb(y): # คืนจำนวนวันของเดือนกุมภาพันธ์ในปี y
    _bc = y
    if (_bc%4==0 and _bc%100!=0) or (_bc%4==0 and _bc%100==0 and _bc%400==0):
        return 29
    else:
        return 28
    return
def days_in_month(m,y): # คืนจำนวนวันของเดือน m ในปี y
    _bc = y
    dct1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dct2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if (_bc%4==0 and _bc%100!=0) or (_bc%4==0 and _bc%100==0 and _bc%400==0):
        return dct2[m]
    else:
        return dct1[m]
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1)
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2)
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days
def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader
def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
    ('0'+str(m))[-2:] + ':' + \
    ('0'+str(s))[-2:]
def to_sec(h,m,s):
    sum_sec = h*3600 + m*60 + s
    return sum_sec
def to_hms(s):
    hour = s//3600
    s = s%3600
    _min = s//60
    s = s%60
    sec = s
    return hour,_min,sec
def diff(h1,m1,s1,h2,m2,s2):
    if s2>=s1:
        sa = s2-s1
        if m2>=m1:
            ma = m2-m1
            ha = h2-h1
        else:
            ma = m2-m1+60
            ha = h2-h1-1
    else:
        sa = s2-s1+60
        m2 -= 1
        if m2>=m1:
            ma = m2-m1
            ha = h2-h1
        else:
            ma = m2-m1+60
            ha = h2-h1-1
    
    return ha,ma,sa
def main():
    hms_start = input()
    hms_end = input()
    t = hms_start.split(':')
    x = hms_end.split(':')
    ans = diff(int(t[0]),int(t[1]),int(t[2]),int(x[0]),int(x[1]),int(x[2]))
    print(hms2str(ans[0],ans[1],ans[2]))
exec(input()) # DON'T remove this line

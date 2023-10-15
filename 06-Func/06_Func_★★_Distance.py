def distance1(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    d1 = ((dx)**2 + (dy)**2)**0.5
    return d1
def distance2(p1, p2):
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    d2 = ((dx)**2 + (dy)**2)**0.5
    return d2
def distance3(c1, c2):
    dx = c2[0]-c1[0]
    dy = c2[1]-c1[1]
    d3 = ((dx)**2 + (dy)**2)**0.5
    if c2[2] >= d3-c1[2] or c1[2] >= d3-c2[2]:
        return d3,True
    return d3,False

def perimeter(points):
    _sum = 0
    for i in range(len(points)-1):
        _sum += distance2(points[i],points[i+1])
    _sum += distance2(points[-1],points[0])
    return _sum
exec(input().strip()) 
def frame(points,i,j):
  x = min(float(points[i][0]),float(points[j][0]))
  y = max(float(points[i][1]),float(points[j][1]))
  w = abs(max(float(points[j][0]),float(points[i][0])) - x)
  h = abs(y - min(float(points[j][1]),float(points[i][1])))

  return [x,y,w,h] # เมื่อ x,y เป็นพิกัดของจุดบนซ้าย w,h เป็นความกว้างและความสูงของเฟรมตามลำดับ


def middle(points,i,j):
  x = (float(points[i][0])+float(points[j][0]))/2
  y = (float(points[i][1])+float(points[j][1]))/2
  return [x,y] # เมื่อ x,y เป็นพิกัดของจุดกึ่งกลางของจุด i,j ในลิสต์ points


def frame_area(points,i,j):
  x = min(float(points[i][0]),float(points[j][0]))
  y = max(float(points[i][1]),float(points[j][1]))
  w = abs(max(float(points[j][0]),float(points[i][0])) - x)
  h = abs(y - min(float(points[j][1]),float(points[i][1])))
  a = w*h

  return float(a) # เมื่อ a เป็นพื้นที่ของเฟรม


def distance(points,i,j):
  d = ((float(points[i][0])-float(points[j][0]))**2+(float(points[i][1])-float(points[j][1]))**2)**0.5
  return d # เมื่อ d เป็นระยะห่างระหว่างจุด i,j ในลิสต์ points


def intersection(points,p1,p2,p3,p4):
  
  return [x,y] # เมื่อ x,y เป็นพิกัดของจุดตัดของส่วนของเส้นตรง p1,p2 กับ p3,p4

point_input = input().strip('[]').split(',')
points = []
for i in range(1,len(point_input),+2):
    points.append([point_input[i-1],point_input[i]])

print(frame(points,1,3))
print(middle(points,0,2))
print(frame_area(points,1,3))
print(distance(points,1,2))
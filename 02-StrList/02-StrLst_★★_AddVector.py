u = input().strip('[]').split(',')
v = input().strip('[]').split(',')

print([float(u[0]),float(u[1]),float(u[2])],"+",[float(v[0]),float(v[1]),float(v[2])],"=",[float(u[0])+float(v[0]),float(u[1])+float(v[1]),float(u[2])+float(v[2])])
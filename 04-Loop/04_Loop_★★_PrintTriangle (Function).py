def print_triangle(h):
    print("."*(h-1)+"*")
    for i in range(h-1,1,-1):
        j = h-i
        print("."*(i-1)+"*"+"."*(2*j-1)+"*")
    print("*"*(2*h-1))
    
exec(input()) # DON'T remove this line
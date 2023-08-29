def sqrt_n_times(x, n):
    for i in range(n):
        x = x**0.5
    return x
 
def cube_root(y):
    y = sqrt_n_times(y,2)*sqrt_n_times(y,4)*sqrt_n_times(y,6)*sqrt_n_times(y,8)*sqrt_n_times(y,10)*sqrt_n_times(y,12)*sqrt_n_times(y,14)*sqrt_n_times(y,16)
    return y
def main():
 q = float(input())
 print(cube_root(q))

exec(input()) # DON'T remove this line
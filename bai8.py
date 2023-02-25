def bai8(n):
    if n == 1 :
        return 1
    return n * bai8(n-1)

x = 0.5
eps = 0.000000001
mu = 3
tu = 3
mau = 4
first = 0.5
count =0
n = 0
temp = 0
second = first + 0.5*x ** mu/mu
print("x =",second)
while abs(first - second) > eps:
    mu+=2
    count += 1
    n=count
    temp= (0.5)*x ** mu/mu
    first = second
    while n>0:
        temp =temp*(tu/mau)
        tu= tu+2
        mau=mau+2
        n -= 1
    second = first + temp
print("Bai 8 Ket Qua = ", second)
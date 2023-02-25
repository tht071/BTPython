def bai10(n):
    if n == 1 :
        return 1
    return n * bai10(n-1)
x = 0.5
eps = 0.000000001
mu = 3
dau =-1
first = x
second = first - x ** mu / mu
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x ** mu / mu)
    dau = - dau
print("Bai 10 Ket qua = ",second)
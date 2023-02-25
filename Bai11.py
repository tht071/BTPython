def bai11(n):
    if n == 1 :
        return 1
    return n * bai11(n-1)
x = 0.5
eps = 0.000000001
mu = 2
dau =-1
first = 0.5
second = first - x ** mu / mu
while abs(first - second) > eps:
    mu-=-1
    first = second
    second = first - (dau * x ** mu / mu)
    dau = - dau
print("Bai 11 Ket Qua = ",second)
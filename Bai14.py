def bai14(n):
    if n == 1 :
        return 1
    return n * bai14(n-1)

x = 0.5
eps = 0.000000001
mu = 2
first = 1
second = first + x ** mu / bai14(mu)
while abs(first - second) > eps:
        mu+=2
        first = second
        second = first +x ** mu / bai14(mu)
print("Bai 14 Ket Qua = ",second)

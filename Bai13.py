def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n-1)

x = 0.5
eps = 0.000000001
mu = 3
first = x
second = first + x**mu / fac(mu)
while abs (first - second) > eps :
    mu +=2
    first = second
    second = first + x**mu / fac(mu)
print("Bai 13 Ket Qua = ", second)
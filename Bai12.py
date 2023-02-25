def bai12(n):
    if n == 1 :
        return 1
    return n * bai12(n-1)
x = 0.5
eps = 0.000000001
mu = 3
first = x
second = first + x ** mu / mu
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first +x ** mu / mu
print("Bai 12 ket qua = ",2*second)
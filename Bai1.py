first = 1
x = 0.5
eps = 0.000001
mu =1
second = first + x**mu / mu
count = 0
while abs(first - second) > eps:
    mu -= -1
    first = second
    second = first + x**mu / mu
    count+=1
print("Bai 1 ket qua = ", second)
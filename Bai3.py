def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

first = 0.5
x = 0.5
temp = 2
eps = 0.000001
second = -1*first - (x*temp/temp)
while abs(first - second) > eps:
    temp -= -1
    first = second
    second = first - (x*temp/temp)
print("Bai 3 ket qua = ", second)
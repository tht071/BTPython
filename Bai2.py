first = 1
x = 0.5
temp = 1
dau = -1
eps = 0.000001
second = first + dau*(((temp + 1)*(temp + 2))/2)*x*temp
while abs(first - second) > eps:
    temp -= -1
    dau = -dau
    first = second
    second = first + dau*(((temp + 1)*(temp + 2))/2)*x*temp
print("Bai 2 ket qua = ", second)
#Bai1
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

#Bai2
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

#Bai3
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

#Bai4
def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.000001
n = 0
temp = (0.5) * x**mu
second = first + (0.5) * x**mu
while abs(first - second) > eps:
    tu = 1
    mau = 4
    mu -= 1
    n = mu
    temp = (0.5) * x**mu
    first = second
    while(n>1):
        temp = temp * (tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    second = first + dau * temp
    dau = -dau
print("Bai 4 ket qua = ", second) 

#Bai5
def bai5(n):
    if n == 1 :
        return 1
    return n * bai5(n-1)
first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.000001
n = 0
temp = 0
second = first - (0.5)*x ** mu
while abs(first - second) > eps:
    tu = 3
    mau = 4
    mu-=-1
    n=mu
    temp= (0.5)*x ** mu
    first = second
    while n>1:
        temp =temp*(tu/mau)
        tu= tu+2
        mau=mau+2
        n -= 1
        dau = - dau
    second = first + dau*temp

print("Bai 5 ket qua = ",second)

#Bai6
def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.00001
mu = 3
dau = -1
first = 0.5
second = first - x**mu / fac(mu)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print ("Bai 6 ket qua = ", second)

#Bai7
def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.000001
mu = 2
dau = -1
first = 1
second = first - x**mu / fac(mu)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print("Bai 7 ket qua = ", second)

#Bai8
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


#Bai9
def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.000001
mu = 1
dau = -1
first = 1
second = first - x**(mu + 1) / fac(mu + 2)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**(mu + 1) / fac(mu + 2))
    dau = -dau
print("Bai 9 ket qua = ", second)

#Bai10
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

#Bai11
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


#Bai12
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

#Bai13
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

#Bai14
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



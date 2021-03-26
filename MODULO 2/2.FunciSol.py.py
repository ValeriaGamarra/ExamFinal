## Ejer 1 ##

def valida_par(a):
    if a % 2 == 0:
        print('el numero es par',a)
    else:
        print('el numero es impart',a)

a=int(input("Ingresa un numero:" ))
resultado = valida_par(a)
print(resultado)

## Ejer 2 ##

def area_rectangulo (base,altura):
    return (base * altura) / 2

b= 15
a=10

area=area_rectangulo(b, a)
print(area)

##Ejer 3 ##
def relacion(a,b):
    if a > b :
        return 1
    elif a < b:
        return -1
    else: 
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

##Ejerc 4 ##
def factorial(num):
    print('Valor inicial -> ',num)
    if num > 1:
        num = num * factorial(num -1)
    print('valor final - >',num)
    return num

print(factorial(5))
 
##Ejer 5 ##
a, b = 0, 1

while b < 50:
    print(b)

    a, b = b,a +b


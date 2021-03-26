###EJERCICIO 1##
saldo= float(input("Escribe tu numero: "))
pago1= (1+0.04)*saldo
pago2=(1+0.04)*pago1
pago3=(1+0.04)*pago2
print(pago1," ",pago2," ",pago3)


###EJERCICIO 2##
import math
a = int(input("Escribe el coeficiente: "))
b = int(input("Escribe el coeficiente: "))
c = int(input("Escribe el coeficiente: "))
discri = b**2-(4*a*c)
if discri >= 0:
    if discri >0:
        raiz1 = (-b+math.sqrt(discri))/(2*a)
        raiz2 = (-b-math.sqrt(discri))/(2*a)
        print(raiz1, raiz2)
    else:
        raiz_unica = -b/(2*a)
        print(raiz_unica)
else:
    print("Ecuación no presenta solución real")


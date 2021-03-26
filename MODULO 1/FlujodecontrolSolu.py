##Problm 3 ##
contra=input("Escriba su contraseña:")
contra= contra.lower()
seg=input("Ingresa nuevamente tu contraseña:")
seg= seg.lower()

if contra == seg:
    print("Las contraseñas coinciden")
else: 
    print("Las contraseñas no coinciden")

##Problm 4 ##
a=int(input("Ingrese un numero :"))
if a % 2 ==0:
    print("Es par",a)
else: 
    print("Es impar",a)

##Problm 5 ##
renta= int(input("Mi renta es:"))

if renta < 10000 :
    print("Su impuesto es de 5%: ",renta*0.05)
elif renta > 10000 and renta < 20000 :
    print("Su impuesto es de 15%: ",renta*0.15)
elif renta > 20000 and renta < 35000 :
    print("Su impuesto es de 20%: ",renta*0.20)
elif renta > 35000 and renta < 60000 :
    print("Su impuesto es de 30%: ",renta*0.30)
if renta > 60000 :
    print("Su impuesto es de 45%: ",renta*0.45)   

##Problm 7##
Elija=input("Elija un  ingrediente extra, la mozarella y tomate ya vienen agregados:")
if Elija == "Pimienta" :
    print("Su pizza es vegetariana")
elif  Elija == "Tofu":
    print("Su pizza es vegetariana")
else:
    print("Su pizza no es vegetariana")

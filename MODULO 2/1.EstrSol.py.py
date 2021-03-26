##Problm 1 ##
repeticiones = int(input( "¿ Cuantos numeros quieres introducir?:"))
suma = 0

for x in range(repeticiones):
    suma += float(input("Introduce un numero: "))

print("Se han introducido",repeticiones,"numeros que en total han sumado",suma,"y la media es",suma/repeticiones)
##Problm 3 ##
def es_primo(numero):
    if numero == 1:
        return False
    elif numero ==2:
        return True
    else:
        for i in range(2,numero):
            if numero % i == 0:
               return False

        return True

for i in range(1,101):
    print(i,es_primo(i))

##Problm 4## 
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']    

lista_3 =[]

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)
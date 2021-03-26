cantidad =int(input('Ingrese la altura del triangulo: '))
for n in range( 1 , cantidad +1):
  print(" " *(cantidad-n)+ '#' * (n))
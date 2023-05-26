# Terminal
import math
print("Que necesitas\t")
opcion = input("1- Animarme\n2- Calcular\n3- Sortir\n\nIntroduce la opcion que necesites:\t")
# Inicio del programa
while opcion != 3:
# Animarme
  if opcion := 1:
    nombre = input("\nDame un nombre porfis:\t")
    nomguion = ""
    for letra in nombre:
      print("Dame una "+letra)
      nomguion = nomguion + letra + '-'
    print(nomguion[:-1].upper())
  if opcion := 2:
    operacion = input("Que quieres calcular")
    if '+' in operacion: 
      numero1 = operacion [:operacion.index('+')]
      numero1 = ("\nIntroduce el primer numero de la suma:")
      numero2 = ("Introduce el segundo numero de la suma")
      print(math.sum(numero1, numero2))
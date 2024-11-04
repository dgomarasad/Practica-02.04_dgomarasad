#Escribir un programa que pregunte al usuario los números ganadores de la
#lotería primitiva, los almacene en una lista y los muestre por pantalla
#ordenados de menor a mayor.
numeros_ganador_1 = int(input('Cual es el primer numero ganador:'))
numeros_ganador_2 = int(input('Cual es el segundo numero ganador:'))
numeros_ganador_3 = int(input('Cual es el tercero numero ganador:'))
numeros_ganador_4 = int(input('Cual es el caurto numero ganador:'))
numeros_ganador_5 = int(input('Cual es el quinto numero ganador:'))
lista = [numeros_ganador_1,numeros_ganador_2,numeros_ganador_3,
         numeros_ganador_4,numeros_ganador_5]
lista.sort()
print('Los numeros ganadores son',lista)



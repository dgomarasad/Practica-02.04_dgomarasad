#Escribir un programa que pida al usuario una palabra y muestre por pantalla
#si es un palíndromo.
palabra = input('Dime una palabra:')
if palabra == palabra [::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")
#Escribir un programa que pida al usuario una palabra y muestre por pantalla
#el número de veces que contiene cada vocal.
palabra = input("Dime una palabra:")
vocales = "aeiou"
for vocal in vocales:
    contador = palabra.count(vocal)
    print("La vocal",vocal,"aparece",contador,"veces")
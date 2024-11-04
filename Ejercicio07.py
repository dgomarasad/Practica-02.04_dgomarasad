#Escribir un programa que almacene el abecedario en una lista, elimine
#de la lista las letras que ocupen posiciones múltiplos de 3, y muestre
# por pantalla la lista resultante.
abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Eliminar letras en posiciones múltiplos de 3 recorriendo de atrás hacia adelante
for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:
        del abecedario[i]

# Mostrar la lista resultante
print("Lista de letras sin posiciones múltiplos de 3:", abecedario)
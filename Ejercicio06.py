#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al
#usuario la nota que ha sacado en cada asignatura y elimine de la lista las
#asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
#asignaturas que el usuario tiene que repetir.
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia','Lengua']
for asignatura in asignaturas[:]:  # Usamos una copia de la lista para poder modificar la original
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota >= 5:  # Si la nota es 5 o superior, eliminamos la asignatura de la lista
        asignaturas.remove(asignatura)

# Mostramos las asignaturas que el usuario tiene que repetir
if asignaturas:
    print("Debes repetir las siguientes asignaturas:", asignaturas)
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
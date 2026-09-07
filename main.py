print("Hola, mundo!")

print("--- INGRESO DE NOTAS DEL CURSO ---")

x = 0

while x == 0:
    for i in range(1, 4):
        print("Ingrese nota " + str(i) + ": ")
        nota = int(input())

    estudiante = input("¿Necesita ingresar nuevo estudiante? (s/n): ")

    if estudiante == 's':
        x = 0
    else:
        x = 1
students = []
while True:
    try:
        num_students = int(input("Ingrese cuantos estudiantes desee: "))
        if num_students <= 0:
            print("El numero de estudiantes debe ser positivo")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un numero valido")
for i in range(num_students):
    print(f"Registro del estudiante #{i+1}")
    name = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            notes_amount = int(input("Cantidad de notas que desea ingresar: "))
            break
        except ValueError:
            print("Por favor, ingrese un numero valido")
        else:
            for i in range(notes_amount):
                print(f"Registro de la nota #{i+1}")





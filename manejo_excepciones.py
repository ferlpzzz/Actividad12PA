students = []
while True:
    try:
        num_students = int(input("Ingrese cuántos estudiantes desea: "))
        if num_students <= 0:
            print("El número de estudiantes debe ser positivo")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido")
for i in range(num_students):
    print(f"\nRegistro del estudiante #{i + 1}")
    name = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            notes_amount = int(input("Cantidad de notas que desea ingresar: "))
            if notes_amount <= 0:
                print("Debe ingresar al menos una nota")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido")
    notes = []
    for j in range(notes_amount):
        while True:
            try:
                note = float(input(f"Ingrese la nota #{j + 1}: "))
                if note < 0:
                    print("La nota no puede ser un número negativo")
                    continue
                notes.append(note)
                break
            except ValueError:
                print("Por favor, ingrese un número válido")

    students.append({
        "nombre": name,
        "notas": notes
    })
print("\nRESULTADOS:")
for student in students:
    try:
        if not student["notas"]:
            print(f"{student['nombre']}: No tiene ninguna nota registrada")
            continue
        average = sum(student["notas"]) / len(student["notas"])
        print(f"{student['nombre']}: Promedio = {average:.2f}")
    except ZeroDivisionError:
        print(f"{student['nombre']}: No se puede calcular promedio (división por cero)")
    except TypeError:
        print(f"{student['nombre']}: Error en los datos de notas")
    except Exception as e:
        print(f"{student['nombre']}: Ocurrió un error inesperado - {type(e).__name__}")






"""
Sistema de Gestión de Estudiantes (SGE) básico
Lenguaje: Python 3
Descripción: Aplicación de consola para gestionar estudiantes con operaciones
             de agregar, mostrar, buscar por ID y salir del sistema.
"""

# ============================================================
# ESTRUCTURA DE DATOS: Lista para almacenar estudiantes
# Se elige lista por su flexibilidad dinámica (no necesita tamaño fijo)
# ============================================================
lista_estudiantes = []

# Variable especial de CONTEO: lleva el total de estudiantes registrados
contador_estudiantes = 0

# Variable especial de BANDERA: controla la salida del bucle principal
bandera_salir = False


# ============================================================
# FUNCIÓN: Mostrar datos de un estudiante individual
# Unidad de código reutilizable para evitar repetición
# ============================================================
def mostrar_estudiante(estudiante):
    """Muestra los datos formateados de un estudiante."""
    print("-" * 40)
    print(f"  ID       : {estudiante['id']}")
    print(f"  Nombre   : {estudiante['nombre']}")
    print(f"  Apellido : {estudiante['apellido']}")
    print(f"  Edad     : {estudiante['edad']} años")
    print(f"  Carrera  : {estudiante['carrera']}")
    print("-" * 40)


# ============================================================
# FUNCIÓN: Mostrar menú principal
# ============================================================
def mostrar_menu():
    """Despliega el menú principal del sistema."""
    print("\n" + "=" * 40)
    print("   SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 40)
    print("  1. Agregar estudiante")
    print("  2. Mostrar todos los estudiantes")
    print("  3. Buscar estudiante por ID")
    print("  4. Salir del sistema")
    print("=" * 40)


# ============================================================
# FUNCIÓN: Agregar un nuevo estudiante
# Usa if para validar entradas y evitar datos incorrectos
# ============================================================
def agregar_estudiante():
    """Agrega un nuevo estudiante a la lista."""
    global contador_estudiantes  # Variable de conteo (uso especial)

    print("\n--- AGREGAR NUEVO ESTUDIANTE ---")

    # Validación del nombre (no vacío)
    nombre = input("  Nombre    : ").strip()
    if nombre == "":
        print("  [ERROR] El nombre no puede estar vacío.")
        return

    apellido = input("  Apellido  : ").strip()
    if apellido == "":
        print("  [ERROR] El apellido no puede estar vacío.")
        return

    # Validación de la edad (debe ser número entero positivo)
    try:
        edad = int(input("  Edad      : "))
        if edad <= 0 or edad > 120:
            print("  [ERROR] La edad debe estar entre 1 y 120.")
            return
    except ValueError:
        print("  [ERROR] La edad debe ser un número entero.")
        return

    carrera = input("  Carrera   : ").strip()
    if carrera == "":
        print("  [ERROR] La carrera no puede estar vacía.")
        return

    # Incrementar conteo y generar ID automático
    contador_estudiantes += 1
    nuevo_id = contador_estudiantes

    # Crear diccionario del estudiante y agregarlo a la lista
    nuevo_estudiante = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera
    }
    lista_estudiantes.append(nuevo_estudiante)

    print(f"\n  [OK] Estudiante agregado exitosamente con ID: {nuevo_id}")


# ============================================================
# FUNCIÓN: Mostrar todos los estudiantes
# Usa for (iteración ascendente) para recorrer la lista
# ============================================================
def mostrar_todos():
    """Muestra todos los estudiantes registrados en el sistema."""
    print("\n--- LISTA DE ESTUDIANTES REGISTRADOS ---")

    # Decisión simple: verificar si hay estudiantes
    if len(lista_estudiantes) == 0:
        print("  No hay estudiantes registrados aún.")
        return

    print(f"  Total de estudiantes: {contador_estudiantes}\n")

    # Iteración ASCENDENTE con for para recorrer la lista
    for estudiante in lista_estudiantes:
        mostrar_estudiante(estudiante)


# ============================================================
# FUNCIÓN: Buscar estudiante por ID
# Usa while con bandera y if para controlar la búsqueda
# ============================================================
def buscar_por_id():
    """Busca un estudiante específico por su número de ID."""
    print("\n--- BUSCAR ESTUDIANTE POR ID ---")

    if len(lista_estudiantes) == 0:
        print("  No hay estudiantes registrados para buscar.")
        return

    try:
        id_buscar = int(input("  Ingrese el ID a buscar: "))
    except ValueError:
        print("  [ERROR] El ID debe ser un número entero.")
        return

    # Variable BANDERA para indicar si se encontró el estudiante
    encontrado = False
    indice = 0  # Variable de control para iteración

    # Iteración con while condicionada al comienzo
    while indice < len(lista_estudiantes) and not encontrado:
        # Decisión simple: comparar el ID
        if lista_estudiantes[indice]["id"] == id_buscar:
            encontrado = True  # Activar bandera
        else:
            indice += 1  # Avanzar al siguiente elemento

    # Decisión simple: verificar resultado de la búsqueda
    if encontrado:
        print("\n  [OK] Estudiante encontrado:")
        mostrar_estudiante(lista_estudiantes[indice])
    else:
        print(f"\n  [INFO] No se encontró ningún estudiante con ID: {id_buscar}")


# ============================================================
# PROGRAMA PRINCIPAL
# Usa while condicionado al comienzo con bandera de salida
# Usa if/elif (decisión múltiple) para el menú
# ============================================================
def main():
    global bandera_salir

    print("\n  Bienvenido al Sistema de Gestión de Estudiantes")

    # Estructura de REPETICIÓN condicionada al comienzo (while)
    # Controlada por la BANDERA bandera_salir
    while not bandera_salir:
        mostrar_menu()

        opcion = input("\n  Seleccione una opción (1-4): ").strip()

        # Estructura de DECISIÓN MÚLTIPLE (if/elif equivalente a switch)
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_todos()
        elif opcion == "3":
            buscar_por_id()
        elif opcion == "4":
            # Cambiar la bandera para salir del bucle
            bandera_salir = True
            print("\n  Gracias por usar el SGE. ¡Hasta pronto!\n")
        else:
            # Manejo de opción inválida
            print("\n  [ERROR] Opción no válida. Por favor seleccione entre 1 y 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
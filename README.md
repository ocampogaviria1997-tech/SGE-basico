# 🎓 Sistema de Gestión de Estudiantes (SGE) básico

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Completo-brightgreen?style=for-the-badge)
![Course](https://img.shields.io/badge/Materia-Algoritmos%20y%20Programación-1A2B5A?style=for-the-badge)

> Aplicación de consola desarrollada en Python 3 para gestionar registros de estudiantes.  
> Proyecto de la asignatura **Algoritmos y Programación** — Universidad Compensar.

---

## 📋 Tabla de contenido

- [Descripción](#-descripción)
- [Funcionalidades](#-funcionalidades)
- [Estructuras de control utilizadas](#-estructuras-de-control-utilizadas)
- [Variables especiales](#-variables-especiales)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Uso del sistema](#-uso-del-sistema)
- [Casos de prueba](#-casos-de-prueba)
- [Análisis Big-O](#-análisis-big-o)
- [Autor](#-autor)

---

## 📌 Descripción

El **SGE básico** es una aplicación por consola (sin interfaz gráfica) que permite registrar, consultar y buscar información de estudiantes de forma sencilla. Fue diseñado para demostrar el dominio de:

- Sentencias de **decisión** simples, anidadas y múltiples (`if`, `elif`, `else`)
- Sentencias de **repetición** condicionadas al comienzo (`while`, `for`)
- Uso especial de **variables**: conteo, bandera e iteración
- **Estructuras de datos simples**: lista dinámica de diccionarios
- **Funciones reutilizables** (principio DRY)
- **Validación robusta** de entradas del usuario

---

## ✅ Funcionalidades

| # | Opción | Descripción |
|---|--------|-------------|
| 1 | **Agregar estudiante** | Registra nombre, apellido, edad y carrera con validación completa |
| 2 | **Mostrar todos** | Lista todos los estudiantes almacenados con su ID único |
| 3 | **Buscar por ID** | Localiza un estudiante específico por su número de identificación |
| 4 | **Salir** | Termina la ejecución de forma controlada mediante una bandera |

---

## 🔁 Estructuras de control utilizadas

```python
# 1. Repetición condicionada al comienzo con BANDERA — bucle principal
while not bandera_salir:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

# 2. Decisión múltiple — equivalente a switch/case
if opcion == "1":
    agregar_estudiante()
elif opcion == "2":
    mostrar_todos()
elif opcion == "3":
    buscar_por_id()
elif opcion == "4":
    bandera_salir = True  # Activa bandera de salida

# 3. Iteración ascendente — recorrer lista completa
for estudiante in lista_estudiantes:
    mostrar_estudiante(estudiante)

# 4. Repetición con bandera — búsqueda por ID
while indice < len(lista_estudiantes) and not encontrado:
    if lista_estudiantes[indice]["id"] == id_buscar:
        encontrado = True
    else:
        indice += 1

# 5. Manejo de excepciones — entradas no numéricas
try:
    edad = int(input("Edad: "))
except ValueError:
    print("[ERROR] La edad debe ser un número entero.")
```

---

## 🔢 Variables especiales

| Variable | Tipo | Propósito |
|----------|------|-----------|
| `contador_estudiantes` | **Conteo** | Incrementa con cada registro; genera IDs únicos automáticamente |
| `bandera_salir` | **Bandera** | Controla el ciclo de vida del bucle principal (`False` → activo, `True` → salir) |
| `encontrado` | **Bandera** | Detiene el bucle de búsqueda al localizar el ID |
| `indice` | **Control de iteración** | Apuntador manual para búsqueda por posición en la lista |

---

## 📁 Estructura del proyecto

```
SGE-basico/
│
├── mainSGE.py          # Código fuente principal
├── README.md           # Este archivo
└── docs/
    └── SGE_Informe_Completo.docx   # Documentación técnica completa
```

---

## 🛠 Requisitos

- **Python 3.8** o superior
- Sin dependencias externas — usa únicamente la librería estándar de Python

Verificar versión instalada:
```bash
python3 --version
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/ocampogaviria1997-tech/SGE-basico.git
cd SGE-basico
```

### 2. Ejecutar el programa
```bash
python3 mainSGE.py
```

En Windows:
```bash
python mainSGE.py
```

---

## 💻 Uso del sistema

Al iniciar, el programa muestra el menú principal:

```
==========================================
    SISTEMA DE GESTIÓN DE ESTUDIANTES
==========================================
  1. Agregar estudiante
  2. Mostrar todos los estudiantes
  3. Buscar estudiante por ID
  4. Salir del sistema
==========================================

  Seleccione una opción (1-4):
```

### Ejemplo — Agregar un estudiante
```
  Seleccione una opción (1-4): 1

  --- AGREGAR NUEVO ESTUDIANTE ---
  Nombre    : Carlos
  Apellido  : Rodríguez
  Edad      : 20
  Carrera   : Ingeniería de Sistemas

  [OK] Estudiante agregado exitosamente con ID: 1
```

### Ejemplo — Buscar por ID
```
  Seleccione una opción (1-4): 3

  --- BUSCAR ESTUDIANTE POR ID ---
  Ingrese el ID a buscar: 1

  [OK] Estudiante encontrado:
  ------------------------------------------
  ID       : 1
  Nombre   : Carlos
  Apellido : Rodríguez
  Edad     : 20 años
  Carrera  : Ingeniería de Sistemas
  ------------------------------------------
```

### Validación de entradas
```
  Nombre    :          ← (Enter sin texto)
  [ERROR] El nombre no puede estar vacío.

  Edad      : abc      ← (texto en lugar de número)
  [ERROR] La edad debe ser un número entero.
```

---

## 🧪 Casos de prueba

| ID | Caso | Entrada | Resultado esperado | Estado |
|----|------|---------|-------------------|--------|
| CP-01 | Agregar estudiante válido | Carlos / Rodríguez / 20 / Ing. Sistemas | ID=1 asignado | ✅ OK |
| CP-02 | Agregar segundo estudiante | Laura / Gómez / 22 / Administración | ID=2 asignado | ✅ OK |
| CP-03 | Mostrar lista completa | Opción 2 tras CP-01 y CP-02 | 2 registros mostrados | ✅ OK |
| CP-04 | Buscar ID existente | ID = 1 | Datos de Carlos Rodríguez | ✅ OK |
| CP-05 | Buscar ID inexistente | ID = 99 | Mensaje 'no encontrado' | ✅ OK |
| CP-06 | Mostrar lista vacía | Opción 2 sin registros | Mensaje 'sin registros' | ✅ OK |
| CP-07 | Nombre vacío | Enter directo | [ERROR] nombre vacío | ✅ OK |
| CP-08 | Edad no numérica | Edad = 'abc' | [ERROR] ValueError capturado | ✅ OK |
| CP-09 | Edad fuera de rango | Edad = -5 o 200 | [ERROR] rango inválido | ✅ OK |
| CP-10 | ID no numérico | ID = 'abc' | [ERROR] ValueError capturado | ✅ OK |
| CP-11 | Opción inválida de menú | Opción = '9' | [ERROR] opción inválida | ✅ OK |
| CP-12 | Salir del sistema | Opción = 4 | Cierre limpio | ✅ OK |

---

## 📊 Análisis Big-O

| Operación | Complejidad | Notas |
|-----------|-------------|-------|
| `agregar_estudiante()` → `list.append()` | **O(1)** amortizado | Inserción al final de la lista |
| `mostrar_todos()` → `for` loop | **O(n)** | Se visita cada registro una vez |
| `buscar_por_id()` → `while` lineal | **O(n)** peor caso | Mejora posible: O(1) con dict hash |
| `mostrar_menu()` | **O(1)** | Texto fijo, no depende de n |
| Validaciones de entrada | **O(1)** | Comparaciones y conversiones constantes |

> **n** = número de estudiantes registrados en el sistema.

**Mejora potencial para búsqueda** (no implementada en esta versión básica):
```python
# O(n) actual → O(1) con diccionario indexado por ID
indice_por_id = {}
indice_por_id[nuevo_id] = nuevo_estudiante  # O(1)
resultado = indice_por_id.get(id_buscar)    # O(1)
```

---

## 👤 Autor

**[Nombre del Estudiante]**  
Universidad Compensar — Facultad de Ingeniería y Tecnología  
Materia: Algoritmos y Programación  
Instructor: [Nombre del Instructor]  
Fecha: Mayo 2025

---

## 📚 Referencias

- Trejos Buriticá, O. I. (2023a). Capítulo 7: Decisiones. En *Probabilidades y matemáticas aplicadas* (pp. 159-178). Ediciones de la U.
- Trejos Buriticá, O. I. (2023b). Capítulo 8: Ciclos. En *Probabilidades y matemáticas aplicadas* (pp. 179-200). Ediciones de la U.
- Trejos Buriticá, O. I. (2020c). Lección 5: Sentencias repetitivas. En *Introducción a la programación con Python* (pp. 37-42). Ediciones de la U.
- Trejos Buriticá, O. I. (2020d). Lección 6: Funciones. En *Introducción a la programación con Python* (pp. 43-48). Ediciones de la U.

---

<p align="center">
  Desarrollado con 🐍 Python 3 · Universidad Compensar · 2025
</p>

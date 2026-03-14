# ==========================================
# 1. IMPORTACIONES
# ==========================================
from Profesores import Profesor
from Materias import Sección, Materia

# ==========================================
# 2. FUNCIONES DEL SISTEMA
# ==========================================
def mostrar_lista_profesores(lista_de_profesores):
    if len(lista_de_profesores) == 0:
        print("\nLa lista de profesores está vacía.")
        return

    print("\n--- LISTA DE PROFESORES ---")
    for i in lista_de_profesores:
        print(f"Nombre: {i.nombre}")
        print(f"Cédula: V-{i.cédula}")
        print(f"Correo: {i.correo}")
        print(f"Número de clases permitidas: {i.n_clases_permitidas}")
        print("Materias que da:")
        if len(i.materias_que_da) == 0:
            print("   (Ninguna materia asignada aún)")
        else:
            for x in i.materias_que_da:
                print(f"   - {x.nombre} ({x.código})")
        print("-" * 30)

def agregar_profesor(lista_profesores, lista_materias):
    print("\n--- AGREGAR NUEVO PROFESOR ---")
    while True:
        nombre_temp = input("Ingrese el nombre y apellido del profesor: ")
        if nombre_temp.replace(" ", "").isalpha() and nombre_temp.strip() != "":
            break
        else: 
            print("Error: El nombre no puede contener caracteres distintos a letras.")
            
    while True:
        cédula_temp = input("Ingrese la cédula del profesor (solo números, ej. 32624143): ")
        if cédula_temp.isdigit() == True and len(cédula_temp) == 8:
            break
        else: 
            print("Error: La cédula debe tener exactamente 8 números.")
            
    correo_temp = nombre_temp.strip().lower().replace(" ", ".") + "@correo.unimet.edu.ve"
    print(f"El correo del profesor será: {correo_temp}")
    
    while True:
        nmaterias_temp = input("Ingrese el número de materias que puede dar el profesor: ")
        if nmaterias_temp.isdigit() == True:
            break
        else: 
            print("Error: Debe ingresar un número.")
            
    lmaterias = []
    while True:
        materia_temp = input("Ingrese el código de las materias que puede dar \n([f] para finalizar): ")
        if materia_temp.lower() == "f": 
            break
        exito = False
        for i in lista_materias:
            if i.código == materia_temp.upper():
                lmaterias.append(i)
                print("Materia agregada correctamente.")
                exito = True
                break
        if not exito: 
            print("Error: Código incorrecto.")
            
    nuevo_profe = Profesor(nombre_temp.title(), int(cédula_temp), correo_temp, int(nmaterias_temp), lmaterias)
    lista_profesores.append(nuevo_profe)
    print("\n¡Profesor agregado con éxito!")

def ver_profesor_especifico(lista_profesores):
    print("\n--- BUSCAR PROFESOR ---")
    if len(lista_profesores) == 0:
        print("No hay profesores registrados.")
        return
    cedula_buscar = input("Ingrese la cédula del profesor a buscar: ")
    encontrado = False
    for p in lista_profesores:
        if str(p.cédula) == cedula_buscar.strip():
            print("\n¡Profesor encontrado!")
            print(f"Nombre: {p.nombre}\nCédula: V-{p.cédula}\nCorreo: {p.correo}")
            encontrado = True
            break
    if not encontrado:
        print(f"\nError: No se encontró profesor con cédula {cedula_buscar}.")

def mostrar_lista_materias(lista_materias):
    if len(lista_materias) == 0:
        print("\nLa lista de materias está vacía.")
        return
    print("\n--- LISTA DE MATERIAS ---")
    for m in lista_materias:
        print(f"Materia: {m.nombre}")
        print(f"Código: {m.código}")
        print("-" * 30)

def agregar_materia(lista_materias):
    print("\n--- AGREGAR NUEVA MATERIA ---")
    while True:
        nombre_temp = input("Ingrese el nombre de la materia: ")
        if nombre_temp.strip() != "": break
        else: print("Error: El nombre no puede estar vacío.")

    while True:
        codigo_temp = input("Ingrese el código de la materia (ej. BPSTP05): ")
        if codigo_temp.replace(" ", "").isalnum() and codigo_temp.strip() != "":
            codigo_temp = codigo_temp.replace(" ", "").upper()
            break
        else: print("Error: Código inválido.")

    while True:
        creditos_temp = input("Ingrese la cantidad de créditos (solo números): ")
        if creditos_temp.isdigit(): break
        else: print("Error: Debe ingresar un número.")
            
    nueva_materia = Materia(nombre_temp.capitalize(), codigo_temp, [], int(creditos_temp))
    lista_materias.append(nueva_materia)
    print("\n¡Materia agregada con éxito!")

# ==========================================
# 3. DATOS DE PRUEBA
# ==========================================
profesores = [
    Profesor("Carlos Bastidas", 32624143, "bastidas.carlos@correo.unimet.edu.ve", 10, []),
    Profesor("Pepito Perez", 30536548, "perez.pepito@correo.unimet.edu.ve", 15, [])
]

secciones = [
   Sección("Algoritmos y programación", "BPSTP05-1", profesores[0]),
   Sección("Algoritmos y programación", "BPSTP05-2", profesores[1])
]

materias = [ 
    Materia("Algoritmos y programación", "BPSTP05", secciones[0:2], 4),
    Materia("Matemática básica", "FBTMM01", [], 4)
]

# ==========================================
# 4. MENÚ PRINCIPAL
# ==========================================
while True:
    print("\n=== BIENVENIDO AL SISTEMA ===")
    print("   1. Ver la lista de profesores.")
    print("   2. Ver un profesor específico.")
    print("   3. Ver la lista de materias.")
    print("   4. Agregar un profesor.")
    print("   5. Agregar una materia.")
    print("   6. Salir.")
    
    s = input("\nAcción a realizar: ")

    if s == "1": mostrar_lista_profesores(profesores)
    elif s == "2": ver_profesor_especifico(profesores)
    elif s == "3": mostrar_lista_materias(materias)
    elif s == "4": agregar_profesor(profesores, materias)
    elif s == "5": agregar_materia(materias)
    elif s == "6": 
        print("¡Hasta luego!")
        break
    else: print("Opción inválida.")
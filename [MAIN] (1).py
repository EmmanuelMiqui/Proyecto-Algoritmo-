# ==========================================
# 1. IMPORTACIONES
# ==========================================
from Profesores import Profesor
from Materias import Sección, Materia

# ==========================================
# 2. FUNCIONES DEL MENÚ
# ==========================================
def mostrar_lista_profesores(lista_de_profesores):
    """
    Recorre una lista de profesores e imprime sus datos.
    Entrada: Lista de objetos Profesor.
    """
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
        
        # Si no tiene materias, mostramos un mensaje
        if len(i.materias_que_da) == 0:
            print("   (Ninguna materia asignada aún)")
        else:
            for x in i.materias_que_da:
                print(f"   - {x.nombre} ({x.código})")
        print("-" * 30)


def agregar_profesor(lista_profesores, lista_materias):
    """
    Pide al usuario los datos para crear un nuevo profesor,
    lo valida y lo agrega a la lista general de profesores.
    """
    print("\n--- AGREGAR NUEVO PROFESOR ---")
    while True:
        nombre_temp = input("Ingrese el nombre y apellido del profesor: ")
        # Validamos que solo tenga letras y no esté vacío
        if nombre_temp.replace(" ", "").isalpha() and nombre_temp.strip() != "":
            break
        else: 
            print("Error: El nombre no puede contener caracteres distintos a letras.")
            
    while True:
        cédula_temp = input("Ingrese la cédula del profesor (solo números, ej. 32624143): ")
        if cédula_temp.isdigit() == True:
            if len(cédula_temp) == 8:
                break
            else: 
                print("Error: El número de cédula debe contener exactamente 8 caracteres.")
        else: 
            print("Error: La cédula no puede contener caracteres que no sean números.")
            
    # Generación automática del correo
    correo_temp = nombre_temp.strip().lower().replace(" ", ".") + "@correo.unimet.edu.ve"
    print(f"El correo del profesor será: {correo_temp}")
    
    while True:
        nmaterias_temp = input("Ingrese el número de materias que puede dar el profesor: ")
        if nmaterias_temp.isdigit() == True:
            break
        else: 
            print("Error: El valor solicitado no puede contener caracteres que no sean números.")
            
    lmaterias = []
    while True:
        materia_temp = input("Ingrese el código de las materias que puede dar el profesor \n([f] para finalizar): ")
        if materia_temp.lower() == "f": 
            break
            
        exito = False
        for i in lista_materias:
            if i.código == materia_temp:
                lmaterias.append(i)
                print("Materia agregada correctamente.")
                exito = True
                break
                
        if exito == False: 
            print("Error: Código incorrecto.")
            
    # Creamos el objeto Profesor y lo agregamos a la lista (¡con los paréntesis en title()!)
    nuevo_profe = Profesor(nombre_temp.title(), int(cédula_temp), correo_temp, int(nmaterias_temp), lmaterias)
    lista_profesores.append(nuevo_profe)
    print("\n¡Profesor agregado con éxito!")

# ==========================================
# 3. DATOS DE PRUEBA (Tus listas)
# ==========================================
profesores = [
    Profesor("Carlos Bastidas", 32624143, "bastidas.carlos@correo.unimet.edu.ve", 10, []),
    Profesor("Pepito Perez", 30536548, "perez.pepito@correo.unimet.edu.ve", 15, [])
]

secciones = [
   Sección("Algoritmos y programación", "BPSTP05-1", profesores[0]),
   Sección("Algoritmos y programación", "BPSTP05-2", profesores[1]),
   Sección("Matemática básica", "FBTMM01-1", profesores[1]),
   Sección("Matemática básica", "FBTMM01-2", profesores[0]),
   Sección("Pensamiento computacional", "FBTSP04-1", profesores[0])
]

materias = [ 
    Materia("Algoritmos y programación", "BPSTP05", secciones[0:2], 4),
    Materia("Matemática básica", "FBTMM01", secciones[2:4], 4),
    Materia("Pensamiento computacional", "FBTSP04", secciones[4:5], 4)
]

# ==========================================
# 4. MENÚ PRINCIPAL
# ==========================================
while True:
    print("\n=== BIENVENIDO AL SISTEMA ===")
    print("Seleccione la operación que desee realizar:")
    print("   1. Ver la lista de profesores.")
    print("   2. Ver un profesor específico.")
    print("   3. Ver la lista de materias.")
    print("   4. Agregar un profesor a la lista.")
    print("   5. Agregar una materia a la lista.")
    print("   6. Salir del sistema.")
    
    s = input("\nAcción a realizar: ")

    if s == "1":
        mostrar_lista_profesores(profesores)
        
    elif s == "2":
        print("Función en construcción...")
        # Aquí llamarías a tu función para buscar un profesor específico
        
    elif s == "3":
        print("Función en construcción...")
        # Aquí llamarías a mostrar_lista_materias(materias)
        
    elif s == "4":
        agregar_profesor(profesores, materias)
        
    elif s == "5":
        print("Función en construcción...")
        # Aquí llamarías a agregar_materia(materias, profesores)
        
    elif s == "6":
        print("Saliendo del sistema... ¡Hasta luego!")
        break
        
    else:
        print("Opción inválida. Intente de nuevo ingresando un número del 1 al 6.")
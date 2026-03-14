from Profesores import *
while True:
    s = input("Bienvenido al sistema. Seleccione la operación que desee realizar.\n" 
    "(Ingrese el indice de la acción a seleccionar y presione [enter].)\n" 
    "   1. Ver la lista de profesores.\n"
    "   2. Ver un profesor específico. \n" 
    "   3. Ver la lista de materias.\n" 
    "   4. Agregar un profesor a la lista.\n" 
    "   5. Agregar una materia a la lista.\n" 
    "   6. Salir del sistema.\n"
    "\n"
    "Acción a realizar: ")
    print('')

    if s == "1":
       Profesor.lista_profesores()
    if s =="3":
          Profesor.agregar_profesor()



from Materias import *
class Profesor: #[MÓDULO DE PROFESORES]
    def __init__(self, nombre, cédula, correo, n_clases_permitidas, materias_que_da):   #Dedino sus atributos.
        self.nombre =              nombre               #"Str"
        self.cédula =              cédula               #int
        self.correo =              correo               #"nombre@correo.unimet.com.ve"
        self.n_clases_permitidas = n_clases_permitidas  #int
        self.materias_que_da =     materias_que_da      #[lista]

    def obtener_nombre(cédula):                                          #Función: Obtener el nombre de un profesor con su número de cédula. Entrada: Cédula(int), Salida: Nombre(str).
        for i in profesores:                                             #Se busca en la lista de profesores.
            if i.cédula == cédula:                                       #Si la entrada coincide con la cédula de algún objeto (profesor) en la lista:
                return print(f'{i.nombre}.')                             #Devuelve el nombre del profesor al que le pertenece la cédula.
        return print("El número de cédula proporcionado no existe.\n")   #Si no se encuentra la cédula, devuelve un mensaje de error.
    
    def obtener_cédula(nombre):                                    #Función: Obtener la cédula de un profesor con su nombre. Entrada: Nombre(str), Salida: Cédula(int).                              
        for i in profesores:                                       #(Esta función es la inversa de la anterior, por lo que se aplica su mismo método).
            if i.nombre == nombre:                                 
                return print(f"V-{i.cédula}.")                     #Retorno del valor de la cédula, junto al formato de ciudadano natural "V-"
            return print("El nombre proporcionado no existe.\n")   #Mensaje de error en caso de que el nombre proporcionado no se encuentre en la lista de profesores.
    
    def datos(i):
        print(f"Nombre: {i.nombre}. \nCédula: V-{i.cédula}. \nCorreo: {i.correo} \nNúmero de clases permitidas: {i.n_clases_permitidas}. \nMaterias que da:")
        for x in i.materias_que_da:
            print(f"   {x.nombre} ({x.código}).")
            print("")
            break        

    def lista_profesores():   #Función: Imprimir una lista ordenada los atributos del objeto "Profesor."
        for i in profesores:  #Se recorre la lista de profesores y se sacan los atributos de cada uno.
             print(f"Nombre: {i.nombre}. \nCédula: V-{i.cédula}. \nCorreo: {i.correo} \nNúmero de clases permitidas: {i.n_clases_permitidas}. \nMaterias que da:")
             for x in i.materias_que_da:
                 print(f"   {x.nombre} ({x.código}).")
            
             print("")

    def agregar_profesor():
            while True:                                                                                       #Se mantiene en un bucle hasta que se cumpla la condicion deseada.
                nombre_temp = input("Ingrese el nombre y appellido del profesor: ")                           #Entrada del nombre.
                if nombre_temp.replace(" ", "").isalpha() and nombre_temp.strip() != "":                      #Se usan dos funciones, una para eliminar los espacios de la entrada y otra para validar que no hayan caracteres distintas de números.
                   break                                                                                      #Se rompe el bucle While "True:"
                else: print("Error: El nombre no puede contener caracteres distintos a letras.")              #Si no se cumple la condición, se imprime el mensaje de error y se repite el bucle.                        
            while True:                                                                                       #En este segmento se aplica lo mismo al anterior pero para la entrada de la cédula.
                cédula_temp = (input("Ingrese la cédula del profesor (solo numeros, ej. 32624143): "))        #Entrada de la cédula.
                if cédula_temp.isdigit() == True:                                                             #Si la entrada es solo de digitos...
                    if len(cédula_temp) == 8:                                                                 #Si la longitud de la entrada es distinto a 8...
                        break                                                                                 #Se rompe el bucle.
                    else: print("El número de cédula debe contener 8 caracteres.")                            #Mensaje de error en caso de que la longitud del string sea distinta a 8.
                else: print("Error: La cédula no puede contener caracteres que no sean números.")             #Mensaje de error en caso de que la entrada contenga caracteres distintos a números.
            correo_temp = nombre_temp.strip().lower().replace(" ", ".") + "@correo.unimet.edu.ve"             #Se crea el correo del profesor con base en el nombre dado anteriormente, cambiando a minusculas las letras, reemplazando los espacios por puntos y agregando el dominio del correo institucional de la universidad.
            print(f"El correo del profesor será: {correo_temp}")                                              #Se imprime un mensaje informando al usuario el correo generado.                             
            while True:                                                                                  
                nmaterias_temp = (input("Ingrese el número de materias que puede dar el profesor: "))         #Se aplica la misma lógica de los segmentos anteriores.
                if nmaterias_temp.isdigit() == True:  
                    break                                                                          
                else: print("Error: El valor solicitado no puede contener caracteres que no sean números.")   #Mensaje de error en caso de que se ingresen caracteres incorrectos.    
            lmaterias = []                                                                                                                       #Definimos una lista vacia donde almacenaremos las materias que dará el profesor. 
            while True:               
                materia_temp = input("Ingrese el código de las materias que puede dar el profesor \n(Ingrese los caracteres [m] para consultar la lista de materias disponibles, [p] para verificar la lista de materias agregadas al profesor y [f] para finalizar): ")
                exito = False
                for i in materias:
                        if i.código == materia_temp:
                            lmaterias.append(i)
                            print("Materia agregada correctamente.")
                            exito = True
                            break
                if exito == False: print("Error: Código incorrecto.")
                if materia_temp == "p": 
                    p = Profesor(nombre_temp.title, cédula_temp, correo_temp, nmaterias_temp, lmaterias)
                    print(lmaterias)
                    del p
                if materia_temp == "f": break
            profesores.append(Profesor(nombre_temp.title, cédula_temp, correo_temp, nmaterias_temp, lmaterias))
                            
profesores = [
    Profesor("Carlos Bastidas", 32624143, "bastidas.carlos@correo.unimet.edu.ve", 10, []),
    Profesor("Pepito Perez", 30536548, "perez.pepito@correo.unimet.edu.ve", 15, [])
]

#Código de prueba: Profesores

"""

while True:
    Profesor.obtener_nombre(32624143)
    Profesor.obtener_cédula("Carlos Bastidas")
    Profesor.lista_profesores()
    Profesor.agregar_profesor()

"""
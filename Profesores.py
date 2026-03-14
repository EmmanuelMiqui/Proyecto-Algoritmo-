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

 
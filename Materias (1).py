class Sección: #[MÓDULO DE MATERIAS 1: CLASE SECCIONES]                                      
    def __init__(self, nombre, código, profesores):  #Defino la clase de secciones, primero que la de materias, ya que las materias están compuestas de secciones.
        self.nombre =     nombre       #Str (nombre de la materia)
        self.código =     código       #STR ([Código de la materia]-[número de la sección]) ej.: BPSTP05-03 (materia x, sección 03).
        self.profesores = profesores   #[Lista]


class Materia: #[MÓDULO DE MATERIAS 2: CLASE MATERIAS]
    def __init__(self, nombre, código, secciones, créditos):
        self.nombre =    nombre      #Str (nombre de la materia)
        self.código =    código      #STR (Código de la materia) ej.: BPSTP05
        self.secciones = secciones   #[Lista]
        self.créditos =  créditos    #int


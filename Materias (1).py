from Profesores import profesores

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

secciones = [
   Sección("Algoritmos y programación", "BPSTP05-1", profesores[0]),
   Sección("Algoritmos y programación", "BPSTP05-2", profesores[1]),
   Sección("Matemática básica", "FBTMM01-1", profesores[1]),
   Sección("Matemática básica", "FBTMM01-2", profesores[0]),
   Sección("Pensamiento computacional", "FBTSP04-1", profesores[0]),
   Sección("Pensamiento computacional", "FBTSP04-2", profesores[1]),
]

materias = [ 
    Materia("Algoritmos y programación", "BPSTP05", secciones[0:1],4),
    Materia("Matemática básica", "FBTMM01", secciones[2:4] ,4),
    Materia("Pensamiento computacional", "FBTSP04", secciones[5:6], 4)
]

for i in secciones:
         i.profesores.materias_que_da.append(i)
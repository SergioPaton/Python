import string

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def esta_aprobado(self):
        if self.nota >5:
            print("Esta aprobado")
        else:
            print("Esta suspendido")
    
    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)



alumno = Alumno("Sergio", 7)
print(alumno)
alumno.esta_aprobado()
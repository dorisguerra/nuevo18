# Clase Persona
class Persona: 
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        print(f"Soy {self.nombre}, tengo {self.edad} años.")

# Clase Coche
class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.volante = "clásico"
        self.ruedas = "michelin"
        self.conductor = None
        self.pasajeros = []

    def asignar_conductor(self, persona):
        self.conductor = persona
        print(f"{persona.nombre} es el conductor del coche {self.marca}.")

    def subir_pasajero(self, persona):
        self.pasajeros.append(persona)
        print(f"{persona.nombre} se ha subido al coche {self.marca}.")

    def el_coche(self):
        print(f"Marca: {self.marca}, volante: {self.volante}, ruedas: {self.ruedas}.")
        if self.conductor:
            print(f"El conductor es {self.conductor.nombre}.")
        else:
            print("Sin conductor.")
        if self.pasajeros:
            print("Pasajeros:")
            for p in self.pasajeros:
                print(f"- {p.nombre}")
        else:
            print("Sin pasajeros.")

# Crear personas
persona1 = Persona("Julia", 30)
persona2 = Persona("Lucía", 20)
persona3 = Persona("Joaquín", 35)

# Crear coche
mi_coche = Coche("Seat León")

# Asignar conductor
mi_coche.asignar_conductor(persona1)

# Subir pasajeros
mi_coche.subir_pasajero(persona2)
mi_coche.subir_pasajero(persona3)

# Mostrar estado del coche
mi_coche.el_coche()

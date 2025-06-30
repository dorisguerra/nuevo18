# Clase base: Personaje
class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vidas = 3      
        self.nivel = 5             
        self.inventario = []       

# Clase Guerrero (hereda de Personaje)
class Guerrero(Personaje):
    def golpe_poderoso(self):
        print(f"{self.nombre} ha dado un gran golpe! ¡El daño es doble!")

    def ataque_basico(self):
        print(f"{self.nombre} ataca con un golpe básico.")

# Crear instancia Guerrero
guts = Guerrero("Guts", "guerrero")
print(guts.nombre, guts.rol, guts.puntos_vidas, guts.nivel, guts.inventario)
guts.ataque_basico()
guts.golpe_poderoso()

# Clase Mago (por ejemplo)
class Mago(Personaje):
    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza una bola de fuego mágica.")

# Crear instancia Mago
merlin = Mago("Merlin", "mago")
merlin.lanzar_hechizo()

# Clase Medico
class Medico(Personaje):
    def atiende_pacientes(self):
        print(f"{self.nombre} sana a los heridos.")
        otro_personaje.puntos_vidas += 1
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.puntos_vidas} puntos de vida.")

# Clase base: Personaje
class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vidas = 3
        self.nivel = 5
        self.inventario = []

# Clase Guerrero
class Guerrero(Personaje):
    def golpe_poderoso(self):
        print(f"{self.nombre} ha dado un gran golpe. ¡Daño doble!")

    def ataque_basico(self):
        print(f"{self.nombre} ataca con un golpe básico.")

# Clase Medico
class Medico(Personaje):
    def curar(self, otro_personaje):
        print(f"{self.nombre} cura a {otro_personaje.nombre}.")
        otro_personaje.puntos_vidas += 1
        print(f"{otro_personaje.nombre} ahora tiene {otro_personaje.puntos_vidas} puntos de vida.")

# Crear instancias
guts = Guerrero("Guts", "guerrero")
dr_jor = Medico("Dr. Jor", "médico")

#  el guerrero se hiere (pierde 1 vida)
guts.puntos_vidas -= 1
print(f"{guts.nombre} está herido. Tiene menos {guts.puntos_vidas} puntos de vida.")

# El médico lo cura
dr_jor.curar(guts)


# Crear instancia Medico
dr_jor = Medico("Dr. Jor", "médico")
print(dr_jor.nombre, dr_jor.rol, dr_jor.puntos_vidas, dr_jor.nivel, dr_jor.inventario)
dr_jor.atiende_pacientes()

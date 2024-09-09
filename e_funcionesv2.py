print("Hecho por Cesar Najera 5I")
print("Funciones creadas por el usuario")
# Las funciones
def Mi_lista():
    amigos=["Homero", "Paty", "Lety"]
    for najera in amigos:
        print(najera)


def Mi_tupla():
    sabores=("Uva","Piña","Fresa")
    for disponible in sabores:
        print(disponible)

def Mi_set():
    carros={"Mustang", "Chevrolet", "Ford"}
    for notengo in carros:
        print(notengo)

def Mi_diccionario():
    datos= {
        "Titulo": "Los siete maridos de Evelyn Hugo",
        "Autor": "Taylor Jenkins",
        "Año": "2017"
    }
    for libro in datos:
        print(libro)

# Llamando a funciones
print("Mis conocidos")
Mi_lista()
print("Sabores de hielitos")
Mi_tupla()
print("Carros que no tengo")
Mi_set()
print("Datos para pedir de un libro")
Mi_diccionario()
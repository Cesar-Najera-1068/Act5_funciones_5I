print("Manejo de funciones V1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")

def mensa(msg):
    print(msg)
def escribenc(Nombre,apellido):
    print(Nombre,apellido)
    print(f"Tu nombre completo: {Nombre} {apellido}")
def suma2num(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es:",s
#Llamando a la funcion.
hola_mundo()
mensa("Hola WhatsAPP") #Llama a mensa con un parametro
mensa("El profe me sorprendio enviando mensajes") # Vuelve a llamar la funcion con parametro
escribenc("Cesar", "Najera")
print("Funciones que regresan valores")
print(suma2num(7,3))
print(suma2num(15,45))
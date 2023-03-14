
nombre = 'Christian'
edad = 21
altura = 1.80
peso = 80
ojos = 'Cafes'
dientes = 'Blancos'
cabello = 'Cafe'

print ("Vamos a hablar de %s." % nombre)
print (f"Tiene {edad} años, mide {altura} metros y pesa {peso} kilos.")
print ("De hecho, no es muy pesado.")
print ("Tiene ojos %s y cabello %s." % (ojos, cabello))
print ("Sus dientes son normalmente %s dependiendo del cafe." % dientes)

# Esta linea es un poco complicada, trata de entenderla
print ("Si yo sumo %d, %d y %d obtengo %d." % (edad, altura, peso, edad + altura + peso))

def saludar():
    nombre = input("Cual es tu nombre: ")
    print("Hola", nombre)

def descripcion(edad, altura, peso, ojos, dientes, cabello):
    print ("Vamos a hablar de %s." % nombre)
    print (f"Tiene {edad} años, mide {altura} metros y pesa {peso} kilos.")
    print ("De hecho, no es muy pesado.")
    print ("Tiene ojos %s y cabello %s." % (ojos, cabello))
    print ("Sus dientes son normalmente %s dependiendo del cafe." % dientes)

    # Esta linea es un poco complicada, trata de entenderla
    print ("Si yo sumo %d, %d y %d obtengo %d." % (edad, altura, peso, edad + altura + peso))

def main():
    saludar()
    descripcion(21, 1.80, 80, 'Cafes', 'Blancos', 'Cafe')

if __name__ == "__main__":
    main()




# 
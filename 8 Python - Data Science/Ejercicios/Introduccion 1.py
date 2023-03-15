
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

# Listas
lista1 = [1, 2, 3, 4, 5]

# Tuplas
tupla1 = (1, 2, 3, 4, 5)

# Diccionarios
diccionario1 = {
    "nombre": "Christian",
    "edad": 21,
    "altura": 1.80,
    "peso": 80,
    "ojos": "Cafes",
    "dientes": "Blancos",
    "cabello": "Cafe"
}

# Conjuntos
conjunto1 = {1, 2, 3, 4, 5}

# For
for i in range(10):
    print(i)

for i in range(10, 20):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(20, 10, -2):
    print(i)

# While
i = 0
while i < 10:
    print(i)
    i += 1

# If
if 1 == 1:
    print("1 es igual a 1")

if 1 == 2:
    print("1 es igual a 2")
else:
    print("1 no es igual a 2")

import random

notas = []
for x in range(6):
    notas.append(random.randint(0, 10))

print(notas)

promedio = sum(notas) / len(notas)

if promedio >= 7:
    print("Aprobado")
elif promedio >= 4:
    print("Recuperatorio")
else:
    print("Reprobado")

# Grafico de las notas

import matplotlib.pyplot as plt

x = list(range(1,7))
y = notas

plt.plot(x,y, marker = 'o')
plt.xlabel('Pruebas')
plt.ylabel('Notas')
plt.title('Notas de las Pruebas de Matematicas')
plt.show()


a = 2

if a < 2:               # Si (a) es MENOR a 2, entra en esta condicional
    a = a + 1 
else:                   # Si no cumple la condicion anterior, entra en esta condicional
    a = a + 2           # Como (a) es igual a 2, entra a esta condicion, por lo tanto se realiza la operacion 2 + 2 = 4

if a < 4:               # Si (a) es MENOR a 4, entra en esta condicional
    a = a - 4 
else:                   # Si no cumple la condicion anterior, entra en esta condicional
    a = a + 6           # Como (a) es igual a 4, entra a esta condicion, por lo tanto se realiza la operacion 4 + 6 = 10

print(a)

# 
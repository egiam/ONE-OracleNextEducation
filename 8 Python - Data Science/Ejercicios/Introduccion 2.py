
import pandas as pd 
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

# Cargamos el dataset
dataset = pd.read_csv('db.csv', sep=';')

# Mostramos los datos
print(dataset)

# Mostramos los datos de la columna 'Nombre'
print(dataset['Nombre'])

# Mostramos los datos de la columna 'Nombre' y 'Apellido'
print(dataset[['Nombre', 'Apellido']])

# Mostramos los datos de la columna 'Nombre' y 'Apellido' de la fila 0
print(dataset[['Nombre', 'Apellido']].iloc[0])

# Mostramos los datos de la columna 'Nombre' y 'Apellido' de la fila 0 a la 3
print(dataset[['Nombre', 'Apellido']].iloc[0:3])

# Mostramos los tipos de datos
print(dataset.dtypes)

# Describe
print(dataset.describe())

# Info
print(dataset.info())


# Tuplas
tupla1 = (1, 2, 3, 4, 5)

# Iterando la tupla
for i in tupla1:
    print(i)

# Diccionarios
diccionario1 = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 25}

# Iterando el diccionario
for i in diccionario1:
    print(i)

# Iterando el diccionario con los valores
for i in diccionario1.values():
    print(i)

# Iterando el diccionario con las llaves y los valores
for i, j in diccionario1.items():
    print(i, j)

# diccionario1.keys()
for i in diccionario1.keys():
    print(i)


# Built-in function
# hhtps://docs.python.org/3.6/library/functions.html

# Sumar los valores del diccionario1
print(sum(diccionario1.values()))

# Sacar el promedio de los valores del diccionario1
print(sum(diccionario1.values()) / len(diccionario1))

# Lista de carros
carros = ['Jetta Variant', 'Passat', 'Crossfox']

pd.Series(carros)


for index, row in dataset.interrows():
    if(2020 - row.Año != 0):
        dataset.loc[index, 'km_media'] = row.Kilometraje / (2020 - row.Año)
    else:
        dataset.loc[index, 'km_media'] = 0

dataset['km_media'] = dataset.apply(lambda row: row.Kilometraje / (2020 - row.Año) if (2020 - row.Año != 0) else 0, axis=1)

print(dataset)


dataset.fillna(0, inplace = True)

dataset.query('Cero_km == True')

# Dropna en kilometraje - elimina todas las filas donde en kilometraje tiene nan

dataset.dropna(subset=['Kilometraje'], inplace = True)


# 
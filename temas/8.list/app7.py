# Creacion de listas
# friends = ["Karen", "Kevin", "Jim"]

# Podriamos tener cual tipo de valor en una lista
#friends = ["Karen", 3, True]

# Como acceder a elementos individuales de la lista
#friends = ["Karen", "Kevin", "Jim"]
#Indices:    0         1       2  
#print(friends) # Imprimira la lista completa, tal cual como esta.

#print(friends[0]) # Imprime el elemento ubicado en el indice 0, que seria Karen
#print(friends[2])

# Tambien podriamos acceder al elemento de la lista desde su ultimo elemento 
#print(friends[-1]) # Imprime el ultimo elemento de la lista: Jim
#print(friends[-2])

# Para seleccionar rangos en una lista
#print(friends[1:]) # Me imprime a partir del indice 1 en adelante

friends = ["Karen", "Kevin", "Jim", "Oscar", "Toby"]
#print(friends[1:3]) # Imprimira desde el indice 1, hasta el indice dos

# Modificar elementos de una lista
friends[1] = "Mike"
print(friends[1])

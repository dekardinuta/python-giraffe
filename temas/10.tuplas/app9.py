
#coordinates = (4, 5)
# indices:     0  1
#print(coordinates[0]) # Imprime el indice 0, que corresponde a 4
#print(coordinates[1])

# caracter inmutable de las tuplas
#coordinates[1] = 10
#print(coordinates[1]) # dara error porque las tuplas no se pueden cambiar

# diferencia de tuplas respecto a las listas:
#coordinates = [4, 5]
#coordinates[1] = 10
#print(coordinates)  # en esta caso, si me realiza el cambio porque es una lista

# creacion de una lista de tuplas
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[1])
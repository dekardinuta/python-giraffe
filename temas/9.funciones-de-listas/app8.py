lucky_numbers = [42, 8, 23, 16, 15, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#print(friends)

# Si quiero agregar a la lista mas elementos a partir de otra lista
#friends.extend(lucky_numbers) # Automaticamente tomara cualquier lista que tengamos y sugerira tomarla
#print(friends)

# Tambien podemos agregar elementos individuales a la lista
#friends.append("Creed") # Agregara otro elemento al final de la lista
#print(friends) 

# Si quisiera agregar otro elemento, pero a mitad de la lista:
#friends.insert(1, "Kelly") # Imprimira Kelly a partir del indice 1, y los demas elementos se moveran hacia la derecha
#print(friends)

# Tambien puedo eliminar elementos:
#friends.remove("Jim") # Imprime la lista y elimina el elemento Jim
#print(friends)

# Puedo restablecer completamente la lista:
#friends.clear()
#print(friends)

# Se puede sacar un elemento de la lista
#friends.pop() # Saca el ultimo elemento de la lista
#print(friends)

# Para saber la existencia de un elemento en la lista:
#print(friends.index("Kevin")) # Me indica la existencia del elemento Kevin en la posicion 0
#print(friends.index("Oscar"))
#print(friends.index("Mike"))

# Se puede contar los elementos similares, o repetidos en la lista:
#print(friends.count("Jim")) # Cuenta la cantidad de elementos de un mismo nombre, en la lista

# Ordenar lista
#friends.sort() # Ordenara la lista de forma ascendente
#print(friends)
#lucky_numbers.sort()
#print(lucky_numbers)

# Podemos invertir listas:
#lucky_numbers.reverse()
#print(lucky_numbers)

# Copiar listas:
friends2 = friends.copy()
print(friends2)

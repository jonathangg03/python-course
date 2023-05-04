# numeros = (1, 2, 3) #Tuplas are defined with ()
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])  # create a tupla based on a list
print(punto)

# A tupla is like a list, except that they cannot be modified
# They have all methods and all that list have, except for the ones
# that modify lists

# numeros.pop() This is not valid

menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros  # otros is now a list, not a tupla
print(primero, segundo, otros)

for n in numeros:
    print(n)

# numeros[0] = 5 # It modifies tupla, is not valid

otraLista = list(numeros)  # transform numeros in a list

print(otraLista)

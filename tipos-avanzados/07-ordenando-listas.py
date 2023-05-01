numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort() sort affects the original list
# the 1st arghument is a key, a function to go throught the array
# the 2nd is a boolean to reverse or not
# numeros.sort(reverse=True) It's posible to pass the 2arg without passing the second one

numeros2 = sorted(numeros, reverse=True)
# sorted doesn't affects the original array, so it has to be asigned to a variable
# 1st argument is the list to sort
# 2nd argument is if array will be reversed or not

print(numeros)
print(numeros2)


usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


def ordena(elemento):
    return elemento[1]

# usuarios.sort() this will order by the element inside, but only if the 1st element of each child array is the number


# we must write the name of the parameters
usuarios.sort(key=ordena, reverse=True)

print(usuarios)
# If we have a list of list, sort() method can sort the list, but only if the 1st element
# is a number.

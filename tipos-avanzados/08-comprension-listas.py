usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# The same in one line
# nombres = [usuario[0] for usuario in usuarios]
# [element will return] for  [item] in [array]
# print(nombres)

# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# conditions
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# On fst example we transform, on second, we filter, on 2rd both


# On real life, normally we use comprension list, but we can find code that
# use map and filter

# With map, we create a new list with list(), inside, we use map methode, with 2 parameters
# the 1st one is what we will do with each element, and the 2nd is the array will be affected
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# With filter, is the same, but we define the condition in the return value
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)

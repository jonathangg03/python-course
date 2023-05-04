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
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

# On fst example we transform, on second, we filter, on 2rd both

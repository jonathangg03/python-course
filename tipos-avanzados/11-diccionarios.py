# are like objects in JS. The keys are assigned with ""
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # get a value
print(punto["y"])

# print(punto["lala"]) # if a key doesn't exist, throw key error

punto["z"] = 45  # asign an element to a dictionary

if "lala" in punto:  # validate if a diccionary has a key
    print("Encontré lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
print(punto)

for valor in punto:
    print(valor, punto[valor])
    # valor is just the key, in case we want to iterate a dictionary

for valor in punto.items():  # items() return tuplas
    print(valor)

for llave, valor in punto.items():  # Tuplas can be detructured
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])

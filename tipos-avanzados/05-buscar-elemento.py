mascotas = ["Pelusa", "Pulga", "Pulga", "Felipe", "Chanchito Feliz"]

# array.index() return first index of an array

# print(mascotas.index("Wolfwang")) / this will throw error in python, doesn't return -1

if "Wolfgang" in mascotas:
    # 1st we have to validate if an element is in array
    print(mascotas.index("Wolfwang"))

print(mascotas.count("Pulga"))

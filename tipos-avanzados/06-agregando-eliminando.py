mascotas = ["Wolfgang", "Pelusa", "Pulga",
            "Felipe", "Pulga", "Chanchito feliz"]

mascotas.insert(1, "Melvin")  # Insert an element on any index
# Insert an element at the end of the array
mascotas.append("Chanchito triste")
mascotas.remove("Pulga")  # Remove the first element with that content
mascotas.pop(1)  # Delete element on index 1
del mascotas[0]  # Another way to delete an element
mascotas.clear()

print(mascotas)

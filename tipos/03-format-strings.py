nombre = "Jonathan"
apellido = "García"
#nombre_completo = nombre + " " + apellido
nombre_completo = f"{nombre} {apellido}"
nombre_completo_b = f"{nombre[2]} {apellido} {2 + 4}"
# Using an string after letter f, is like template strings in js, inside {} will be expressions
print(nombre_completo)

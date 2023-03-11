nombre_curso = 'Ultimate Python'
descripción_curso = """
Este tipo de texto es usado
cuando lo que se va a escribir esta 
compuesto dentro de varias
líneas de código 
"""

print(len(nombre_curso))  # string length
print(nombre_curso[0])  # string character at 0 index
print(nombre_curso[0:8])
# part of the string. The 1st number is the start index, and the 2nd is how many characters we will cut
print(nombre_curso[9:])  # from index 9 to the end
print(nombre_curso[:8])  # from index 0 to the number 8
print(nombre_curso[:])  # the whole string

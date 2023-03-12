animal = "    chanchitO feliz  "
print(animal.upper())
print(animal.lower())
print(animal.capitalize())  # if 1st character is a space will be uppercase
print(animal.title())
print(animal.strip())  # remove spaces at the begining and end
print(animal.strip().capitalize())
print(animal.lstrip())  # remove spaces at the begining
print(animal.rstrip())  # remove spaces at the end
print(animal.find("ch"))
# Find the index of the string we write as argument. If doesn't exist, will return -1.
# If there are many, return 1st
print(animal.replace("itO", "j"))
print("cha" in animal)  # If string is in string return true
print("cha" not in animal)  # If string is not in string return true

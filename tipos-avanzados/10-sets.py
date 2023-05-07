# Sets are a kind of lists where values are never repeated
# They are defined with {}
# If there are repeated values, it will ignore the repetition

primer = {1, 1, 2, 2, 3, 4}
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)  # create a set based on a list
# print(segundo)

print(primer | segundo)  # join sets

print(primer & segundo)
# create a set with the values of the 1st set that are in the second

print(primer - segundo)
# create a set with values that are on the 1st and are not in the 2nd

print(primer ^ segundo)
# create a set with the values that they have not in common

if 5 in segundo:
    print("Hola mundo")

# The problem with sets is that we can't get a value from its
# But we can make validations, like the example below

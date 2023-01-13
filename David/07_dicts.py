## Dictionaries ##

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "David",
                 "Apellido": "Morales", "Edad": 25, 1: "Python"}

my_dict = {"Nombre": "David", "Apellido": "Morales",
           "Edad": 25, "Lenguajes": {"Python", "Swift", "Kotlin"},1:"1.77"}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
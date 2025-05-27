name = "Anna"
age = 20

# F-strings
print(f"{name} is {age} years old.")

# str.format method
print("{} is {} years old.".format(name, age))
print("{0} is {1} years old.".format(name, age))
print("{0} is {1} years old. {0} is a student".format(name, age))
print("{name} is {age} years old. {name} is a student".format(
    name=name, age=age))
print("{name} is {age} years old. {name} is a student".format(
    name=name, age=30))
print("{name} is {age} years old. {name} is a student".format(
    name="Jane", age=30))

person_name = "Jane"
print("{name} is {age} years old. {name} is a student".format(
    name=person_name, age=30))
print("{name} is {years_old} years old. {name} is a student".format(
    name=person_name, years_old=30))

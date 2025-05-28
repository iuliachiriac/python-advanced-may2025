from datetime import date


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"<{self.__class__.__name__} name={self.name}>"

    def __lt__(self, other: "Person"):
        return self.date_of_birth > other.date_of_birth


p1 = Person("Anna", date(2000, 5, 6))
p2 = Person("Jane", date(1983, 7, 23))

print(str(p1), repr(p1))
print(p1.__str__(), p1.__repr__())

print(f"{p1.name} is younger than {p2.name}:", p1 < p2)
print(p1.__dict__, Person.__dict__)

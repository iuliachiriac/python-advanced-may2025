from datetime import date


class InvalidDateOfBirth(Exception):
    pass


class Person:
    MIN_YEAR = 1900

    def __init__(self, name, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def date_of_birth(self):  # date_of_birth = property(date_of_birth)
        # print("getter called")
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):
        if value.year < self.MIN_YEAR:
            raise InvalidDateOfBirth(
                f"Date of birth can't be before {self.MIN_YEAR}")
        self._date_of_birth = value

    @date_of_birth.deleter
    def date_of_birth(self):
        # print("deleter called")
        del self._date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (
                self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

    def __str__(self):
        return f"<{self.__class__.__name__} name={self.name}>"

    def __lt__(self, other: "Person"):
        return self._date_of_birth > other.date_of_birth


class Student(Person):
    pass


if __name__ == "__main__":
    p1 = Person("Anna", date(2000, 5, 31))
    p2 = Person("Jane", date(1983, 7, 23))

    print(str(p1), repr(p1))
    print(p1.__str__(), p1.__repr__())

    print(f"{p1.name} is younger than {p2.name}:", p1 < p2)
    print(p1.__dict__, Person.__dict__)

    print(p1._date_of_birth)
    print(p1._Person__date_of_birth)

    try:
        p1.date_of_birth = date(1854, 5, 7)  # setting an attribute
    except InvalidDateOfBirth as ex:
        print("date_of_birth setting failed:", ex)
    print(p1.date_of_birth)  # getting an attribute
    # del p1.date_of_birth

    try:
        p3 = Person("John", date(1854, 5, 7))
    except InvalidDateOfBirth as ex:
        print(ex)

    print(f"{p1.name} is {p1.age} years old.")

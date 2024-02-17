class Person:
    def __init__(self,firstname,age,gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender


    def details(self):
        print(self.firstname, "is studying")

teacher = Person("Francy", 30,"male" )
accountant = Person("Anne", 40,"female" )
doctor = Person("Ben", 50,"male" )

print(teacher.firstname, teacher.age, teacher.gender)
print(accountant.age)

doctor.details()

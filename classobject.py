# CLass is blueprint of a object
# An object is an instance of class

class Person:
    # Properties/Attributes/Characteristics
    name = "Bob"
    Age = 23
    location = "California"

    def speak(self):
        print("Person is speaking")

accountant = Person() # Instantiating an object
print(accountant.Age)

accountant.speak()


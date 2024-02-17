# Parent class

class Animals:
    def speak(self):
        print("Animal is speaking")


# Child Class
class Dog(Animals):
    def bark(self):
        print("Dog is barking")

class Cat(Animals):
    def meaow(self):
        print("Cat is meaowing")

poumba = Animals()
dody = Dog()

bobo = Cat()
bobo.speak()



class animal:
    def speak(self):
        print("Animal is speaking")
    def bark(self):
        print("Animal is barking")
    def eat(self):
        print("Animal are eating")


class Dog(animal):
    def bark(self):
        print("Dog is barking")
    def eat(self):
        print("Dog are eating")

class dogChild(Dog):
    def eat(self):
        print("Puppies are eating")

a = animal()
# a.bark()    # NOT ACCESSIBLE
a.bark()
a.speak()
a.eat()

d = Dog()
d.bark()
d.speak()
d.eat()

dc = dogChild()
dc.bark()
dc.speak()
dc.eat()
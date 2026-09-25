class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
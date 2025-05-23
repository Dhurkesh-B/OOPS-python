class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        return f"I am {self.name} and I am {self.age} years old"
    
    def speak(self):
        return "I dont know who i am"
    
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        return "Meow"

    def show(self):
        return f"Hello, {super().show()} and i am {self.color} in color"
class Dog(Pet):
    def speak(self):
        return "Bark"


p = Pet("Alex",2)
c = Cat("Tom",5,"white")
d = Dog("Tim",3)

print(p.show())
print(c.show())
print(d.show())

print(p.speak())
print(c.speak())
print(d.speak())

print(c.show())
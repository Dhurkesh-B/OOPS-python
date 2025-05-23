class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(f"Name : {self.name} \nAge : {self.age} \nLaptop spec \nBrand : {self.lap.brand} \nCPU : {self.lap.cpu} \nRAM : {self.lap.ram}")

    class Laptop:
        def __init__(self):
            print("Enter this PC details")
            self.brand = input("lap brand : ")                                                       
            self.cpu = input("lap cpu : ")
            self.ram = input("lap ram : ")
    
print("Enter the Student details")
s1 = Student(input("Name : "),int(input("Age : ")))
print("***************************************************")
s1.show()
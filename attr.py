

#          using of direct class variable

# class Person:
#     number_of_person = 0

#     def __init__(self,name):
#         self.name = name
#         Person.number_of_person+=1
    
#     def get_count(self):
#         return Person.number_of_person

# class Student(Person):
#     number_of_person = 100


# p1 = Student("Alex")
# print(p1.name,p1.get_count())
# p2 = Student("John")
# print(p2.name,p2.get_count())








#   using classmethod it works in the inherited class



# class Person:
#     number_of_person = 0
#     def __init__(self,name):
#         self.name = name
#         Person.increment_count()

#     @classmethod
#     def increment_count(cls):
#         cls.number_of_person+=1

#     @classmethod
#     def get_count(cls):
#         return cls.number_of_person
    
# class Student(Person):
#     number_of_person = 100

#     def __init__(self, name):
#         super().__init__(name)
#         Student.increment_count()


# s1 = Student("Alex")
# print(s1.name, s1.get_count())

# s2 = Student("John")
# print(s2.name, s2.get_count())



class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()

Computer.config(com1)
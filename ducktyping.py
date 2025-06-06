class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def getMarks(self):
        return f"M1 : {self.m1}\nM2 : {self.m2}"
    
    def __add__(self,next):
        m1 = self.m1 + next.m1
        m2 = self.m2 + next.m2 
        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,next):
        value1 = self.m1 + self.m2
        value2 = next.m1 + next.m2
        if value1>value2:
            return "yes"
        else:
            return "no"
        
    def __str__(self):

        return f"Hello,\nM1 : {self.m1}\nM2 : {self.m2} "
    
s1 = Student(80,70)
s2 = Student(90,100)

# print(s1.getMarks())
# print('*'*10)
# print(s2.getMarks())
# print('*'*10)
s3 = s1 + s2
# print(s3.getMarks())


# print(s2>s1)

print('-'*10)
print(s1)
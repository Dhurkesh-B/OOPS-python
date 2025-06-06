class Student:
    def total(self,m1 = None,m2 = None,m3 = None):
        if m1 and m2 and m3:
            return m1+m2+m3
        if m1 and m2:
            return m1+m2
        return m1
    
 

s1 = Student()
print(s1.total(100,50,100))
print(s1.total(50,100))
print(s1.total(100))
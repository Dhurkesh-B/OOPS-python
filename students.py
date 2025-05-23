class Students:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_marks(self):
        return self.marks
    
class Course:

    def __init__(self,name,max_limit):
        self.name = name
        self.max_limit = max_limit
        self.students = []
    
    def addStudent(self,student):
        if len(self.students)<self.max_limit:
            self.students.append(student)
            return True
        return False

    def get_average_marks(self):
        value = 0
        for stud in self.students:
            value+=stud.get_marks()
        return value/len(self.students)

s1 = Students("John",19,80)
s2 = Students("Alex",20,85)
s3 = Students("Martin",21,90)

course1 = Course("Science",2)
print(course1.addStudent(s1))
print(course1.addStudent(s2))
print(course1.addStudent(s3))
print(course1.name,*[i.name for i in course1.students],sep="\n")
print("Average score",course1.get_average_marks())

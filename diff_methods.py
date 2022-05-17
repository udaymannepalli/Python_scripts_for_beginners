class Student:
    school = 'python'
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print('This is from student class, static method')
rishi = Student(45,55,100)
bunny = Student(78,88,98)
print(bunny.average())
print(Student.getschool())
Student.info()
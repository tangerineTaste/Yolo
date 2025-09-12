class Student():
    count = 0
    def __init__(self,age,name,stno):
        self.age = age
        self.name = name
        self.stno = stno
        Student.count +=1
    def change_study(self, stno):
        self.stno = stno
    def show_study_name(self,study):
        return study.study_name()


class Study(Student):
    def __init__(self,no,name):
        self.no = no
        self.name = name
        
    def study_name(self):
        return self.name


computer = Study(1, '컴퓨터공학')
machine = Study(2, '기계공학')

student_a = Student(20,'홍길동', 1)
student_b = Student(21,'마길동',2)
student_c = Student(22,'강길동',2)

print('홍길동의 학과:',student_a.show_study_name(computer))
print('총 학생 수:',Student.count)
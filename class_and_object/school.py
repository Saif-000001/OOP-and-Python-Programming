# Use multiple classes to create a school

class Student:
    def __init__(self, name, current_class, id) -> None:
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self, name,subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, subject: {self.subject}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else :
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('------------our teacher-----------')
        for teacher in self.teachers:
            print(teacher)
        print('-------------our student-----------')
        for student in self.students:
            print(student)
        return 'all done!'

phitron = School('phitron')
phitron.enroll('alue', 80)
phitron.enroll('rani', 9800)

phitron.add_teacher('DJ', 'DS')
phitron.add_teacher('JS', 'ALGO')

print(phitron)


# alia = Student('A', 9, 1)
# print(alia)


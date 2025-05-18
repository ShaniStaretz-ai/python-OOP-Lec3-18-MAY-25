from student import Student
class Course:

    def __init__(self, _name, _size, _students=None):
        self.name=_name
        self.size=_size
        if _students is None:
            _students = []
        self.student_list=_students

    def add_student(self,new_student:Student):
        if len(self.student_list)<self.size:
            self.student_list.append(new_student)
            print("the student was added successfully")
        else:
            print(f"sorry dear {new_student.name}, the course is full, no place for new students")
    def __str__(self):
        return f"name:{self.name},size:{self.size},students list:{self.student_list}"

    def print_students_list(self):
        print(self.student_list)

if __name__ == '__main__':
    c1=Course("shani",9)


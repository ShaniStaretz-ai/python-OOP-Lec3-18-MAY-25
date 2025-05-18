import pprint
from person import Person
from student import Student
from course import Course
if __name__ == '__main__':
    # name='shani'
    # print("hello-simple")
    # pprint.pprint(f"hello {name}")
    # pprint.pprint(name)
    p1=Person('shani',50,190)
    p1.print_details()
    p1.print_measurements()
    s1=Student("shani",22,87,37,"kfarSava")
    s2=Student("shani2",22,87,37,"kfarSava")
    s3 = Student("shani3", 22, 87, 37, "Kfar Sava")
    c1= Course()
    print(c1)





class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('School Member Name: ',self.name)
        print('Age : ',self.age)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('Marks : ',self.marks)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary : ',self.salary)

def main():
    print("Inheritance Demonstration : \n")

    obj1 = Student('Swapnil',25, 120)
    obj1.tell()
    print()
    obj2 = Teacher('Mrs Vidya', 45, 120000)
    obj2.tell()


if __name__ == "__main__":
    main()


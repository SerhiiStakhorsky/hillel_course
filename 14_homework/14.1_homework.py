class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}, Record Book: {self.record_book}"


class GroupOverflowError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) >= 10:
            raise GroupOverflowError(f"Cannot add more than 10 students to group {self.number}")
        self.group.add(student)

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza2', 'Taylor', 'AN146')
st4 = Student('Female', 25, 'Liza3', 'Taylor', 'AN147')
st5 = Student('Female', 25, 'Liza4', 'Taylor', 'AN148')
st6 = Student('Female', 25, 'Liza5', 'Taylor', 'AN149')
st7 = Student('Female', 25, 'Liza6', 'Taylor', 'AN150')
st8 = Student('Female', 25, 'Liza7', 'Taylor', 'AN151')
st9 = Student('Female', 25, 'Liza8', 'Taylor', 'AN152')
st10 = Student('Female', 25, 'Liza9', 'Taylor', 'AN153')
st11 = Student('Female', 25, 'Liza10', 'Taylor', 'AN154')

gr = Group('G1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except GroupOverflowError as e:
    print(e)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

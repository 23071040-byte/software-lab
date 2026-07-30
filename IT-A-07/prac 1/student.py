class Student:
    def __init__(self, field_id, name, marks):
        self.field_id = field_id
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade(marks)

    def get_field_id(self):
        return self.field_id

    def set_field_id(self, field_id):
        self.field_id = field_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_marks(self):
        return self.marks

    def set_marks(self, marks):
        self.marks = marks
        self.grade = self.calculate_grade(marks)

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def calculate_grade(self, marks):
        if marks >= 90:
            return 'A'
        elif marks >= 80:
            return 'B'
        elif marks >= 70:
            return 'C'
        elif marks >= 60:
            return 'D'
        else:
            return 'F'

    def to_string(self):
        return f"student{{field_id={self.field_id}, name='{self.name}', marks={self.marks}, grade='{self.grade}'}}"


students = [
    Student(101, "Alice", 92),
    Student(102, "Bob", 84),
    Student(103, "Charlie", 76),
    Student(104, "Diana", 68),
    Student(105, "Ethan", 58),
    Student(106, "Fiona", 90)
]

for student in students:
    print(student.to_string())

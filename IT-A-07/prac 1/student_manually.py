class Student:
    def __init__(self, field_id, name, marks):
        self.field_id = field_id
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    # Getters
    def get_field_id(self):
        return self.field_id

    def get_name(self):
        return self.name

    def get_marks(self):
        return self.marks

    def get_grade(self):
        return self.grade

    # Setters
    def set_field_id(self, field_id):
        self.field_id = field_id

    def set_name(self, name):
        self.name = name

    def set_marks(self, marks):
        self.marks = marks
        self.grade = self.calculate_grade()

    # Grade calculation
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    # toString equivalent
    def __str__(self):
        return (f"ID: {self.field_id}, "
                f"Name: {self.name}, "
                f"Marks: {self.marks}, "
                f"Grade: {self.grade}")


# Creating 6 students
student1 = Student(101, "Alice", 95)
student2 = Student(102, "Bob", 84)
student3 = Student(103, "Charlie", 76)
student4 = Student(104, "David", 68)
student5 = Student(105, "Eva", 59)
student6 = Student(106, "Frank", 91)

# Store in a list
students = [student1, student2, student3, student4, student5, student6]

# Print student details
print("Student Details:")
for student in students:
    print(student)
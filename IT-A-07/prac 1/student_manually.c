#include <stdio.h>
#include <string.h>

// Structure
struct Student {
    int field_id;
    char name[50];
    int marks;
    char grade;
};

// Function to calculate grade
char calculateGrade(int marks) {
    if (marks >= 90)
        return 'A';
    else if (marks >= 80)
        return 'B';
    else if (marks >= 70)
        return 'C';
    else if (marks >= 60)
        return 'D';
    else
        return 'F';
}

// Constructor-like function
struct Student createStudent(int id, char name[], int marks) {
    struct Student s;
    s.field_id = id;
    strcpy(s.name, name);
    s.marks = marks;
    s.grade = calculateGrade(marks);
    return s;
}

// Getters
int getFieldId(struct Student s) {
    return s.field_id;
}

char* getName(struct Student *s) {
    return s->name;
}

int getMarks(struct Student s) {
    return s.marks;
}

char getGrade(struct Student s) {
    return s.grade;
}

// Setter
void setMarks(struct Student *s, int marks) {
    s->marks = marks;
    s->grade = calculateGrade(marks);
}

// toString equivalent
void printStudent(struct Student s) {
    printf("ID: %d, Name: %s, Marks: %d, Grade: %c\n",
           s.field_id, s.name, s.marks, s.grade);
}

int main() {

    // Creating 6 students
    struct Student students[6];

    students[0] = createStudent(101, "Alice", 95);
    students[1] = createStudent(102, "Bob", 84);
    students[2] = createStudent(103, "Charlie", 76);
    students[3] = createStudent(104, "David", 68);
    students[4] = createStudent(105, "Eva", 58);
    students[5] = createStudent(106, "Frank", 91);

    printf("Student Details:\n\n");

    for (int i = 0; i < 6; i++) {
        printStudent(students[i]);
    }

    return 0;
}
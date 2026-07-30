#include <stdio.h>
#include <string.h>
#include <time.h>

typedef struct {
    int field_id;
    char name[50];
    double marks;
    char grade;
} Student;

char calculateGrade(double marks) {
    if (marks >= 90) return 'A';
    if (marks >= 80) return 'B';
    if (marks >= 70) return 'C';
    if (marks >= 60) return 'D';
    return 'F';
}

void initStudent(Student *s, int field_id, const char *name, double marks) {
    s->field_id = field_id;
    strcpy(s->name, name);
    s->marks = marks;
    s->grade = calculateGrade(marks);
}

int getFieldId(const Student *s) {
    return s->field_id;
}

void setFieldId(Student *s, int field_id) {
    s->field_id = field_id;
}

const char *getName(const Student *s) {
    return s->name;
}

void setName(Student *s, const char *name) {
    strcpy(s->name, name);
}

double getMarks(const Student *s) {
    return s->marks;
}

void setMarks(Student *s, double marks) {
    s->marks = marks;
    s->grade = calculateGrade(marks);
}

char getGrade(const Student *s) {
    return s->grade;
}

void setGrade(Student *s, char grade) {
    s->grade = grade;
}

void toString(const Student *s) {
    printf("student{field_id=%d, name='%s', marks=%.2f, grade='%c'}\n",
           s->field_id, s->name, s->marks, s->grade);
}

int main() {
    clock_t start = clock();

    Student students[6];

    initStudent(&students[0], 101, "Alice", 92);
    initStudent(&students[1], 102, "Bob", 84);
    initStudent(&students[2], 103, "Charlie", 76);
    initStudent(&students[3], 104, "Diana", 68);
    initStudent(&students[4], 105, "Ethan", 58);
    initStudent(&students[5], 106, "Fiona", 90);

    for (int i = 0; i < 6; i++) {
        toString(&students[i]);
    }

    clock_t end = clock();
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Execution time: %.6f seconds\n", elapsed);

    return 0;
}

public class StudentManually {

    private int fieldId;
    private String name;
    private double marks;
    private String grade;

    // Default constructor
    public StudentManually() {
    }

    // Parameterized constructor
    public StudentManually(int fieldId, String name, double marks) {
        this.fieldId = fieldId;
        this.name = name;
        this.marks = marks;
        this.grade = calculateGrade();
    }

    // Calculate grade
    private String calculateGrade() {
        if (marks >= 90) {
            return "A";
        } else if (marks >= 80) {
            return "B";
        } else if (marks >= 70) {
            return "C";
        } else if (marks >= 60) {
            return "D";
        } else {
            return "F";
        }
    }

    // Getters
    public int getFieldId() {
        return fieldId;
    }

    public String getName() {
        return name;
    }

    public double getMarks() {
        return marks;
    }

    public String getGrade() {
        return grade;
    }

    // Setter for marks (updates grade automatically)
    public void setMarks(double marks) {
        this.marks = marks;
        this.grade = calculateGrade();
    }

    @Override
    public String toString() {
        return "Student{" +
                "fieldId=" + fieldId +
                ", name='" + name + '\'' +
                ", marks=" + marks +
                ", grade='" + grade + '\'' +
                '}';
    }

    public static void main(String[] args) {

        StudentManually[] students = {
                new StudentManually(1, "Alice", 85.5),
                new StudentManually(2, "Bob", 72.0),
                new StudentManually(3, "Charlie", 95.0),
                new StudentManually(4, "David", 60.0),
                new StudentManually(5, "Eve", 45.0),
                new StudentManually(6, "Frank", 88.0)
        };

        for (StudentManually student : students) {
            System.out.println(student);
        }
    }
}
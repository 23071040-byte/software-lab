public class student {
    private int field_id;
    private String name;
    private double marks;
    private String grade;

    public student() {
    }

    public student(int field_id, String name, double marks) {
        this.field_id = field_id;
        this.name = name;
        this.marks = marks;
        this.grade = calculateGrade(marks);
    }

    public int getField_id() {
        return field_id;
    }

    public void setField_id(int field_id) {
        this.field_id = field_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMarks() {
        return marks;
    }

    public void setMarks(double marks) {
        this.marks = marks;
        this.grade = calculateGrade(marks);
    }

    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public String calculateGrade(double marks) {
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

    @Override
    public String toString() {
        return "student{" +
                "field_id=" + field_id +
                ", name='" + name + '\'' +
                ", marks=" + marks +
                ", grade='" + grade + '\'' +
                '}';
    }

    public static void main(String[] args) {
        student[] students = {
                new student(101, "Alice", 92),
                new student(102, "Bob", 84),
                new student(103, "Charlie", 76),
                new student(104, "Diana", 68),
                new student(105, "Ethan", 58),
                new student(106, "Fiona", 90)
        };

        for (student s : students) {
            System.out.println(s);
        }
    }
}

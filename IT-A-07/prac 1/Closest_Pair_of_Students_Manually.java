public class Closest_Pair_of_Students_Manually{

    public static void main(String[] args) {

        int[] marks = {92, 76, 81, 95, 83};

        int student1 = 0;
        int student2 = 0;
        int minDifference = Integer.MAX_VALUE;

        // Compare every pair of students
        for (int i = 0; i < marks.length; i++) {

            for (int j = i + 1; j < marks.length; j++) {

                int difference = Math.abs(marks[i] - marks[j]);

                if (difference < minDifference) {
                    minDifference = difference;
                    student1 = marks[i];
                    student2 = marks[j];
                }
            }
        }

        System.out.println("Closest Pair:");
        System.out.println(student1 + " and " + student2);
        System.out.println("Minimum Difference = " + minDifference);
    }
}
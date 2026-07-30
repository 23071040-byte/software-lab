import java.util.Arrays;

public class Closest_Pair_of_Student {
    static class PairResult {
        int firstIndex;
        int secondIndex;
        int difference;

        PairResult(int firstIndex, int secondIndex, int difference) {
            this.firstIndex = firstIndex;
            this.secondIndex = secondIndex;
            this.difference = difference;
        }
    }

    public static PairResult findClosestPair(int[] marks) {
        if (marks == null || marks.length < 2) {
            throw new IllegalArgumentException("At least two marks are required.");
        }

        int bestDifference = Integer.MAX_VALUE;
        int firstIndex = -1;
        int secondIndex = -1;

        for (int i = 0; i < marks.length; i++) {
            for (int j = i + 1; j < marks.length; j++) {
                int currentDifference = Math.abs(marks[i] - marks[j]);
                if (currentDifference < bestDifference) {
                    bestDifference = currentDifference;
                    firstIndex = i;
                    secondIndex = j;
                }
            }
        }

        return new PairResult(firstIndex, secondIndex, bestDifference);
    }

    public static void main(String[] args) {
        int[] marks = {92, 76, 81, 95, 83};

        System.out.println("Marks = " + Arrays.toString(marks));
        PairResult result = findClosestPair(marks);

        System.out.println("Closest pair: " + marks[result.firstIndex] + " and " + marks[result.secondIndex]);
        System.out.println("Minimum difference = " + result.difference);
    }
}

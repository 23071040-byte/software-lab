import java.util.HashSet;
import java.util.Set;

public class github_optimized {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 4, 5, 1};

        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for (int num : arr) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }
        

        System.out.println("Duplicate elements are:");
        if (duplicates.isEmpty()) {
            System.out.println("None");
        } else {
            for (int value : duplicates) {
                System.out.println(value);
            }
        }

        System.out.println("Time Complexity: O(n)");
    }
}

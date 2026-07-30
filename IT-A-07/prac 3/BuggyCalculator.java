import java.util.Scanner;

public class BuggyCalculator {

    public static void main(String[] args) {

        // -------------------------
        // BUG 1: Syntax Error - Missing Semicolon
        // -------------------------
        // ORIGINAL: Scanner sc = new Scanner(System.in)
        // THE BUG: Statement is missing a semicolon at the end
        // FIX: Add semicolon to terminate the statement
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Buggy Calculator ===");

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        System.out.println("\nChoose Operation");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Multiply");
        System.out.println("4. Divide");
        System.out.println("5. Average");

        // BUG 2: Syntax Error - Missing Semicolon
        // ORIGINAL: int choice = sc.nextInt()
        // THE BUG: Statement is missing a semicolon at the end
        // FIX: Add semicolon to terminate the statement
        int choice = sc.nextInt();

        switch(choice) {

            case 1:
                System.out.println("Addition = " + add(num1, num2));
                break;

            case 2:
                System.out.println("Subtraction = " + subtract(num1, num2));
                break;

            case 3:
                System.out.println("Multiplication = " + multiply(num1, num2));
                // BUG 3: Logical Bug - Missing Break Statement
                // ORIGINAL: (missing break;)
                // THE BUG: Case 3 falls through to case 4, executing both
                // FIX: Add break; statement to prevent fall-through
                break;

            case 4:
                System.out.println("Division = " + divide(num1, num2));
                break;

            case 5:
                System.out.println("Average = " + average(num1, num2));
                break;

            // BUG 4: Syntax Error - Missing Colon After Default
            // ORIGINAL: default
            // THE BUG: default keyword is missing colon ':' separator
            // FIX: Add colon after default keyword (should be "default:")
            default:
                System.out.println("Invalid Choice");
        }

        // BUG 5: Resource Management Bug - Scanner Not Closed
        // ORIGINAL: (missing sc.close())
        // THE BUG: Scanner resource is not closed, causing resource leak
        // FIX: Close the Scanner by calling sc.close()
        sc.close();
    }

    // -------------------------
    // BUG 6: Syntax Error - Missing Comma in Parameters
    // -------------------------
    // ORIGINAL: static int add(int a int b)
    // THE BUG: Parameters are missing a comma separator
    // FIX: Add comma between parameters (should be "int a, int b")
    static int add(int a, int b) {
        return a + b;
    }

    // -------------------------
    // BUG 7: Logical Bug - Wrong Operator
    // -------------------------
    // ORIGINAL: return a + b;
    // THE BUG: Method adds numbers instead of subtracting them
    // FIX: Change operator from '+' to '-' (should be "a - b")
    static int subtract(int a, int b) {
        return a - b;
    }

    // -------------------------
    // BUG 8: Logical Bug - Semicolon After For Loop
    // -------------------------
    // ORIGINAL: for(int i = 1; i <= b; i++);
    // THE BUG: Semicolon after for loop makes loop body unreachable
    // FIX: Remove semicolon before curly brace (should be "for(int i = 1; i <= b; i++)")
    static int multiply(int a, int b) {

        int result = 0;

        for(int i = 1; i <= b; i++) {
            result += a;
        }

        return result;
    }

    // -------------------------
    // BUG 9: Runtime Bug - Division by Zero
    // -------------------------
    // ORIGINAL: return a / b; (without validation)
    // THE BUG: No check for zero divisor causes ArithmeticException
    // FIX: Add validation to check if b is zero before division
    static int divide(int a, int b) {

        if (b == 0) {
            System.out.println("Error: Cannot divide by zero!");
            return 0;
        }
        return a / b;
    }

    // -------------------------
    // BUG 10: Arithmetic Bug - Integer Division Loss
    // -------------------------
    // ORIGINAL: return (a + b) / 2;
    // THE BUG: Integer division truncates decimal part (e.g., 5/2 = 2 not 2.5)
    // FIX: Cast to double for accurate average or use: (a + b) / 2.0
    static double average(int a, int b) {

        // Integer division instead of decimal average
        return (a + b) / 2.0;
    }

    // -------------------------
    // BUG 11: Runtime Bug - Null Pointer Exception
    // -------------------------
    // ORIGINAL: String name = null; System.out.println(name.length());
    // THE BUG: Calling method on null object causes NullPointerException
    // FIX: Initialize string or add null check before calling methods
    static void nullPointerDemo() {

        String name = "John";  // Initialize with a value
        if (name != null) {    // Or add null check
            System.out.println(name.length());
        }
    }

    // -------------------------
    // BUG 12: Runtime Bug - Array Index Out of Bounds
    // -------------------------
    // ORIGINAL: System.out.println(arr[10]);
    // THE BUG: Array has 5 elements (indices 0-4), accessing index 10 is out of bounds
    // FIX: Use valid index within array bounds (0-4)
    static void arrayBug() {

        int[] arr = new int[5];

        // ArrayIndexOutOfBoundsException - FIXED: Access valid index
        System.out.println(arr[4]);
    }

    // -------------------------
    // BUG 13: Performance Bug - Unnecessary Nested Loops
    // -------------------------
    // ORIGINAL: Nested loops executing 100,000 x 100,000 = 10 billion iterations
    // THE BUG: Loop does nothing but wastes CPU time (O(n²) complexity)
    // FIX: Remove nested loop or add meaningful computation
    static void performanceBug() {

        for(int i = 0; i < 100000; i++) {
            // Fixed: Removed unnecessary nested loop
            // Perform actual computation here instead of empty nested loop
        }
    }

    // -------------------------
    // BUG 14: Input Validation Bug - No Error Handling
    // -------------------------
    // ORIGINAL: int age = sc.nextInt();
    // THE BUG: If user enters non-integer input, InputMismatchException occurs
    // FIX: Add validation check using hasNextInt() before reading
    static void inputBug() {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Age: ");

        if (sc.hasNextInt()) {
            int age = sc.nextInt();
            System.out.println("Age: " + age);
        } else {
            System.out.println("Error: Please enter a valid integer!");
        }
    }
}
/*
 * You are required to compute the power of a number by implementing a calculator. Create a class MyCalculator which consists of a single method long power(int, int). This method takes two integers,  and , as parameters and finds . If either  or  is negative, then the method must throw an exception which says "". Also, if both  and  are zero, then the method must throw an exception which says ""

For example, -4 and -5 would result in .

Complete the function power in class MyCalculator and return the appropriate result after the power operation or an appropriate exception as detailed above.

Input Format

Each line of the input contains two integers,  and . The locked stub code in the editor reads the input and sends the values to the method as parameters.

Constraints

Output Format

Each line of the output contains the result , if both  and  are positive. If either  or  is negative, the output contains "n and p should be non-negative". If both  and  are zero, the output contains "n and p should not be zero.". This is printed by the locked stub code in the editor.

Sample Input 0

3 5
2 4
0 0
-1 -2
-1 3
Sample Output 0

243
16
java.lang.Exception: n and p should not be zero.
java.lang.Exception: n or p should not be negative.
java.lang.Exception: n or p should not be negative.
*/
import java.util.Scanner;
class MyCalculator {
    long power(int n, int p){
        if(n==0 && p==0){
        throw new Exception("n and p should not be zero.");
    }
        if(n < 0 || p < 0){
            throw new Exception("n and p must be positive");
        }else{
            return ((long)Math.pow(n, p))
        }
    }
}

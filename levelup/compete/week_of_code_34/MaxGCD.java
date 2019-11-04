import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class MaxGCD {
    // still times out a lot
    // score: 3.91
    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    static int maximumGcdAndSum(int[] A, int[] B) {
        // Complete this function
        int maxGCD = 0;
        int maxSum = 0;
        int g = 0;
        int s = 0;
            
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                g = gcd(A[i], B[j]);
                if (g > maxGCD) {
                    maxSum = A[i] + B[j];
                    maxGCD = g;
                } else if (g == maxGCD) {
                    s = A[i] + B[j];
                    if (s > maxSum) {
                        maxSum = s;
                    }
                }
            }
        }
        return maxSum;               
    }

    public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] A = new int[n];
    for(int A_i = 0; A_i < n; A_i++){
        A[A_i] = in.nextInt();
    }
    int[] B = new int[n];
    for(int B_i = 0; B_i < n; B_i++){
        B[B_i] = in.nextInt();
    }
    int res = maximumGcdAndSum(A, B);
    System.out.println(res);
    }
}

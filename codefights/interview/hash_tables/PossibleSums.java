import java.util.Arrays;
import java.util.Hashtable;

public class PossibleSums {
    // BRUTE FORCE, but it's Java, which is FAST and EFFICIENT
    // so I passed the tests
    public static void main(String[] args) {
        
        int[] stepState = {0, 0, 0, 0, 0};
        int[] coinsTest = {10, 50, 100, 500};
        int[] quantityTest = {5, 3, 2, 2};
        

        /*
        int[] stepState = {0, 0, 0, 0};
        int[] coinsTest = {5, 10, 20};
        int[] quantityTest = {2, 2, 3};
        */
        
        int res = possibleSums(coinsTest, quantityTest);
        
        System.out.println(res);
    }

    public static int[] step(int[] state, int digit, int[] limit, int[] values) {
        // state[0] is the total
        if (digit == 0) {
            // return new int[] {-1};
            return null;
        }
        System.out.println(Arrays.toString(state));
        if (state[digit] == limit[digit-1]) {
            state[digit] = 0;
            state[0] -= limit[digit-1] * values[digit-1];
            return step(state, digit-1, limit, values);
        }
        state[digit] += 1;
        state[0] += values[digit-1];
        return state;
    }

    public static int possibleSums(int[] coins, int[] quantity) {
        Hashtable<Integer, String> ht = new Hashtable<Integer, String>();
        int numCoins = coins.length;
        int[] state = new int[numCoins+1];
        for (int i = 0; i < numCoins+1; i++) {
            state[i] = 0;
        }

        state = step(state, numCoins, quantity, coins);
        while (state != null) {
            ht.put(state[0], "True");
            state = step(state, numCoins, quantity, coins);
        }
        return ht.size();
        
    }

}
            

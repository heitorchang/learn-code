import java.util.HashSet;
import java.util.Set;

public class FirstDuplicate {
    static int firstDuplicate(int[] a) {
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < a.length; i++) {
            if (set.contains(a[i])) {
                return a[i];
            }
            set.add(a[i]);
        }
        return -1;
    }
    
    public static void main(String[] args) {
        System.out.println();
    }
}

import java.util.*;

public class AllLongestStrings {
    static String[] allLongestStrings(String[] arr) {
        List<String> out = new ArrayList<>();

        // find length of longest
        int longest = 0;
        for (String s : arr) {
            if (s.length() > longest) {
                longest = s.length();
            }
        }

        // filter longest strings
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].length() == longest) {
                out.add(arr[i]);
            }
        }
        return out.toArray(new String[0]);
    }
    
    public static void main(String[] args) {
        String[] input = {"ab", "cd", "e"};
        System.out.println(allLongestStrings(input));
    }
}

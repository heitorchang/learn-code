// 3

public class CheckPalindrome {
    static boolean checkPalindrome(String s) {
        int len = s.length();
        int limit = len / 2;
        char left;
        char right;
        
        for (int i = 0; i < limit; i++) {
            // System.out.println(s.charAt(i));
            left = s.charAt(i);
            right = s.charAt(len - i - 1);
            if (left != right) {
                return false;
            }
        }
        
        return true;
    }
    
    public static void main(String[] args) {
        System.out.println(checkPalindrome("manner"));
        System.out.println(checkPalindrome("trouble"));
        System.out.println(checkPalindrome("racecar"));
    }
}

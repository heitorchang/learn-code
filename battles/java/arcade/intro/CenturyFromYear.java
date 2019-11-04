// 2

public class CenturyFromYear {
    static int centuryFromYear(int year) {
        return ((year - 1) / 100) + 1;
    }
    
    public static void main(String[] args) {
        System.out.println(centuryFromYear(1900));
        System.out.println(centuryFromYear(1988));
    }
}

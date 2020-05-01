/*
  import java.util.List;
  import java.util.ArrayList;
*/

class Splice {
    // removes item at given index

    /* cannot create array of type (generic) T 
    public static <T> T[] splice(T[] orig, int index) {
        int len = orig.length;
        ArrayList<T> spliced = new ArrayList<>();
        
        for (int i = 0; i < index; i++) {
            spliced.add(orig[i]);
        }
        for (int i = index+1; i < len; i++) {
            spliced.add(orig[i]);
        }
        return (T[]) spliced.toArray();
    }
    */

    public static int[] splice(int[] orig, int index) {
        int len = orig.length;
        int[] spliced = new int[len-1];
        
        for (int i = 0; i < index; i++) {
            spliced[i] = orig[i];
        }
        for (int i = index+1; i < len; i++) {
            spliced[i-1] = orig[i];
        }
        return spliced;
    }
    
    
    public static void main(String[] args) {
        int[] intArray = { 0, 1, 2, 3, 4, 5, 6 };
        int[] splicedInt = splice(intArray, 2);

        System.out.println("Spliced int array: ");

        for (var x : splicedInt) {
            System.out.print(x + " ");
        }
    }
}

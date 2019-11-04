// 4

public class AdjacentElementsProduct {
    static int adjacentElementsProduct(int[] inputArray) {
        Integer maxProduct = Integer.MIN_VALUE;
        for (int i = 0, end = inputArray.length - 1; i < end; i++) {
            maxProduct = Math.max(maxProduct, inputArray[i] * inputArray[i+1]);
        }
        return maxProduct;
    }
    
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5};
        System.out.println(adjacentElementsProduct(nums));
    }
}

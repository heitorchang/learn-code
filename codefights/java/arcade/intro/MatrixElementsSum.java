// After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

// Help the bots calculate the total price of all the rooms that are suitable for them.

// Example

// For
// matrix = [[0, 1, 1, 2], 
//           [0, 5, 0, 0], 
//           [2, 0, 3, 3]]
// the output should be
// matrixElementsSum(matrix) = 9.

public class MatrixElementsSum {
    static int fn(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[] haunted = new int[cols];

        int price = 0;
        
        // initialize haunted. 1 = True: haunted, 0 = Not haunted
        for (int i = 0; i < cols; i++) {
            haunted[i] = 0;
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == 0) {
                    haunted[c] = 1;
                }
                if (haunted[c] == 0) {
                    price += matrix[r][c];
                }
            }
        }
        
        return price;
    }
    
    public static void main(String[] args) {
        int[][] test1 = {{0,1,1,2}, {0,5,0,0}, {2,0,3,3}};
        System.out.println(fn(test1));
    }
}

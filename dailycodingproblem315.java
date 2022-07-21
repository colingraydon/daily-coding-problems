// In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

// Here is an example:

// 1 2 3 4 8
// 5 1 2 3 4
// 4 5 1 2 3
// 7 4 5 1 2
// Write a program to determine whether a given input is a Toeplitz matrix.


//I haven't had time to test too many cases but but I suspect it should work for all edge cases
public class dailycodingproblem315 {
   
    public static boolean ToeplitzChecker(int arr[][])
    {
        boolean isToeplitz = true;
        int rows = arr.length;

        int columns = arr[0].length;

        //traversing down the first column
        for (int i = 0; i < rows; i++)
        {
            int holder = arr[i][0];
            int j = 0;
            while (j < rows && j < columns && ((j+i) < rows))
            {
                if (holder != arr[j+i][j])
                {
                    isToeplitz = false;
                }
                j++;
            }
        }
       
        //traversing down first row
        for (int j = 0; j < columns; j++)
        {
            int holder = arr[0][j];
            int i = 0;
            while (i < rows && i < columns && ((j+i) < columns))
            {
                if (holder != arr[i][j+i])
                {
                    isToeplitz = false;
                }
                i++;
            }
        }
        return isToeplitz;
    }
}
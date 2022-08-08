// A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
// return the lowest possible cost.

public class dailycodingproblem19 {

    //this finds the minimum value of the array excluding the kth element
    public static int findMinExclusive(int[] arr, int k)
    {
        int min;
        if (k != 0) min = arr[0];
        else min = arr[1];
        for (int i = 1; i < arr.length; i++)
        {
            if (min > arr[i] && i !=k) min = arr[i];
        }
        return min;
    }

    //finds min value of an array
    public static int findMin(int[] arr)
    {
        int min = arr[0];
        for (int i = 0; i < arr.length; i++)
        {
            if (min < arr[i]) min = arr[i];
        }
        return min;
    }
   
    //the array paintCost is the cost of of paint. the element [n][k] is the cost of painting the nth house the color k
    public static int minCost(int[][] paintCost)
    {
        int numberOfHouses = paintCost.length;
        int numberOfColors = paintCost[0].length;
        //this is the holder array for net cost. element[n][k] represents the total min cost of painting the nth house color k and references the previous min costs
        int arr[][] =  new int[numberOfHouses][numberOfColors];
        //this matches the first house strictly to the color of painting the first house
        for (int i = 0; i < numberOfColors; i++)
        {
            arr[0][i] = paintCost[0][i];
        }
        //this for loop will add the paint cost for a certain color of the ith house to the previous min cost while ensuring that colors don't match
        for (int i = 1; i < numberOfHouses; i++)
        {
            for (int k = 0; k < numberOfColors;k++)
            {
                arr[i][k] = paintCost[i][k] + findMinExclusive(arr[i-1], k);
            }
        }
        //returns the lowest element of the last row of the holder array for net cost
        int totalMinCost = findMin(arr[numberOfHouses - 1]);
        return totalMinCost;
    }
    public static void main(String args[])
    {
        int[][] testArray = { {4,1,2,1}, {3,6,2,5},{2,1,3,1},{7,4,1,3}};
        System.out.println(minCost(testArray));
       
   
    }
}
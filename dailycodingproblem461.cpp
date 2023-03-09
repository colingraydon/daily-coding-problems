// This problem was asked by Facebook.

// There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

// For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

// Right, then down
// Down, then right
// Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

#include <iostream>

// This is a combinatorics problem. ((m-1)+(n-1))! / (m-1)!(n-1)! should be the answer
int getPaths(int m, int n)
{

    int count = 1;
    int i = 1;
    while (i <= m + n - 2)
    {
        count *= i;
        i++;
    }

    i = 1;
    while (i < m || i < n)
    {
        if (i < m && i < n)
        {
            count /= i;
            count /= i;
        }
        else
        {
            count /= i;
        }
        i++;
    }
    return count;
}

int main()
{
    int n = 2;
    int m = 2;
    int ans = getPaths(5, 5);
    std::cout << ans << std::endl;
}
// You are given a string consisting of the letters x and y, such as xyxxxyxyy.
// In addition, you have an operation called flip, which changes a single x to y or vice versa.
// Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
//  In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int flipCounter(string);

int main()
{
    string str = "xyxxxyxyy";
    flipCounter(str);
    return 0;
}

int flipCounter(string str)
{
    int l = str.length();
    int flipsToX[l] = {};
    int flipsToY[l] = {};

    int rightmostX;
    int leftmostY;
    flipsToX[0] = 0;
    flipsToY[l - 1] = 0;

    for (int i = 0; i < l; i++)
    {
        if (str[i] == 'y')
        {
            leftmostY = i;
            break;
        }
    }

    for (int i = l - 2; i > 0; i--)
    {
        if (str[i] == 'x')
        {
            rightmostX = i;
            break;
        }
    }

    int yCount = 0;
    for (int i = leftmostY; i < l; i++)
    {
        if (str[i] == 'x')
        {
            yCount++;
        }
        flipsToY[i] = yCount;
    }

    int xCount = 0;
    for (int i = rightmostX; i > -1; i--)
    {
        if (str[i] == 'y')
        {
            xCount++;
        }
        flipsToX[i] = xCount;
    }

    int minFlips = flipsToX[0] + flipsToY[0];
    for (int i = 1; i < l; i++)
    {
        minFlips = min((flipsToX[i] + flipsToY[i]), minFlips);
    }

    cout << "Min flips is " << minFlips << endl;
    return minFlips;
}
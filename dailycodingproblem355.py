# You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

# Write an algorithm that finds an appropriate Y array with the following properties:

# The rounded sums of both arrays should be equal.
# The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.



def minimize_floating_point(l):

    #creating a list with the difference between every element in L and an integer, then sorting it
    arr = []
    i = 0
    while (i < len(l)):
        temp_value = l[i] % 1
        arr.append([temp_value, l[i], i])
        i += 1
    arr.sort()
    #this is the number of times we will have to round a number up
    total_round_ups = 0
    i = 0
    while (i < len(arr)):
        total_round_ups += arr[i][0]
        i += 1

    #now that we have teh number of times we will need to round a number up, and we have the sorted values of the difference between
    #every element and an integer, we just take the last total_round_ups in the sorted arr and round those up, then find the corresponding initial value and index of all elements
    round_down_index = len(arr) - total_round_ups
    i = 0
    result_arr = []
    while (i < len(arr)):
        result_arr.append(0)
        i += 1
    i = 0
    while (i < len(arr)):
        temp_index = arr[i][2]
        if(i < round_down_index):
            temp_value = arr[i][1] - (arr[i][1] % 1)
        else:
            temp_value = arr[i][1] - (arr[i][1] % 1) + 1
        result_arr[temp_index] = temp_value
        i += 1
    
    return result_arr

print(minimize_floating_point([1.3, 2.3, 4.4]))






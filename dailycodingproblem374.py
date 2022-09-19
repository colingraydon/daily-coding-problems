# Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.

# For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.


def check_arr(arr, i, checked, prev_index, lowest, highest):


    print("method called, prev index = ", prev_index, "i = ", i, "checked =", checked, "highest = ", highest, "lowest = ", lowest)
    temp = arr[i]
    
    temp_prev_index = i


    if (prev_index is not None):
        if (i not in checked):
            if temp == i:
                while (i >= 0 and arr[i-1] == (i-1)):
                    i -= 1
                    return i
            elif (temp > i):
                checked.append(i)
                if (i <= lowest):
                    i = (lowest + i) // 2
                    lowest = i
                else: 
                    i = (prev_index + i) //2
                prev_index = temp_prev_index
                check_arr(arr, i, checked, prev_index, lowest, highest)
            elif (temp < i):
                checked.append(i)
                if (i >= highest):
                    i = (highest + i) // 2
                    highest = i
                else:
                    i = (prev_index + i) // 2
                prev_index = temp_prev_index
                check_arr(arr, i, checked, prev_index, lowest, highest)
        else:
            return None
    else:
        if (temp < i):
            i = (i + len(arr)) //2
            highest = i
            checked.append(temp_prev_index)
            check_arr(arr, i, checked, prev_index, lowest, highest)
        elif (temp > i):
            i = i // 2
            lowest = i
            checked.append(temp_prev_index)
            check_arr(arr, i, checked, prev_index, lowest, highest)



def wrapper(arr):

    n = len(arr)
    i = n // 2
    checked = []
    check_arr(arr, i, checked, prev_index=None, lowest = i, highest = i)








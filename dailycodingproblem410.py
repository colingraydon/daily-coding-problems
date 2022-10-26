# You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

# Write an algorithm that finds an appropriate Y array with the following properties:

def pairwise(arr):


    sorted_arr = []
    for element in arr:
        sorted_arr.append(element)
    sorted_arr.sort()
    sum = 0
    int_sum = 0
    for element in sorted_arr:
        sum += element
        int_sum += int(element)
    index = len(arr) - (sum - int_sum)
    index_value = sorted_arr[int(index)]
    ans = []
    i = 0
    while (i < len(arr)):
        print("in loop, arr[i] is", arr[i])
        temp = int(arr[i])
        if (arr[i] >= index_value):
            temp += 1
        ans.append(temp)
        i += 1
    print(ans)

pairwise([1.3, 2.3, 1.4])

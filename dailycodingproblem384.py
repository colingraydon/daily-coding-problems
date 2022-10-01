# You are given an array of integers representing coin denominations and a total amount of money.
# Write a function to compute the fewest number of coins needed to make up that amount. If it is not possible to make that amount, return null.


def get_change(arr, amount):

    result = -1

    if (amount == 0):

        return 0

    length = len(arr)
    for i in range(0, length):

        if(arr[i] <= amount):
            temp = get_change(arr, amount - arr[i])

        if (result == -1):
            result = 1
        elif (temp + 1 < result):
            result = temp + 1

    return result


# Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

# For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.

#trivial result is achieved by sorting the array and then checking if an element is within 1 of the previous element, and incrementing a counter if so. this is O(n log n)
#the below result is O(n)

def check_sequence(arr):

    s = set()
    result = 0

    for element in arr:

        s.add(element)

    for i in range(len(arr)):

        if arr[i-1] not in s:

            temp = arr[i]
            while (temp in s):
                temp += 1

            subseq_res = temp - arr[i]
            if (subseq_res > result):
                result = subseq_res

    return result

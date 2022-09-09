# Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.

def longest_substring(arr):

    n = len(arr)
    i = 0
    temp = arr[i] - 1
    starting_index = 0
    size = 0
    # maps the first index of the substring to its length
    answer_map = []
    answer_map.append(0)
    answer_map.append(1)
    while(i < n):
        if arr[i] > temp:
            size += 1
            temp = arr[i]
            if (size > answer_map[1]):
                answer_map[0] = starting_index
                answer_map[1] = size
        else:
            starting_index = i
            size = 1
        i += 1
    
    index = answer_map[0]
    length = answer_map[1]
    answer = arr[index:(length+ index)]
    return answer

print(longest_substring([1,2,5,4,8,21, 22, 23, 1]))


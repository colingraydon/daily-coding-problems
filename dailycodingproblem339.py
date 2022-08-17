#Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k.

#This is trivial in O(n^3), but this solution should solve it in O(n^2) via window sliding

def find_sum(l, sum):

    length = len(l)
    l.sort()
    sum_exists = False

    for i in range(0, length - 2):

        j = i+1
        k = length

        while ( j < k ):

            if (l[i] + l[j] + l[k] == sum):
                sum_exists = True
                print("Yes, the 3 elements are", l[i], l[j], l[k])
            elif (l[i] + l[j] + l[k] < sum):
                j += 1
            else:
                k -= 1
    
    if sum_exists is False:
        print("No such entries exist")

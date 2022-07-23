#Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct, find a "peak" element in O(log N) time.

def function(list):
    
    #integer dividing list
    n = len(list) // 2
    if (len(list) > 2):
        if (list[n] > list[n+1] and list[n] < list[n-1]):
            del list[n:]
            function(list)
        if (list[n] > list[n-1] and list[n] < list[n+1]):
            del list[0:n]
            function(list)
            
    #this line is only checking 3 elements at most. the program will run in O(log n). i just used the max method because it is cleanest here
    #strictly speaking, if the initial list is has exactly 3 elements, the program will run in O(n).
    #this can be avoided with the following if statement, however this will slow down operations in larger data sets more than it will help efficiency
    #if len(list) == 3 return list[1]
    m = max(list)    
    return m

function([1, 4, 5, 8, 9, 11, 12, 13, 14, 2])
function([1])
function([1,12,5,4,3,2])
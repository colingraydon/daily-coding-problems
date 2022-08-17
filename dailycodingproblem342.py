# reduce (also known as fold) is a function that takes in an array, a combining function, and an initial value and builds up a result by calling the combining function on each element of the array, left to right. For example, we can write sum() in terms of reduce:

# def add(a, b):
#     return a + b

# def sum(lst):
#     return reduce(lst, add, 0)
# This should call add on the initial value with the first element of the array, and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

# Implement your own version of reduce.

import math
class reducer:

    def add(a,b):

        return a + b

    def subtract(a,b):

        return a - b

    def multiply(a,b):

        return a*b

    def divide(a,b):
        if b == 0:
            return "Divide by 0 error"
        else:
            return a/b

    def mod(a,b):

        return a%b

    def exp(a,b):

        return math.exp(a,b)

    def reduce(l, func, n):

        temp_value = n
        for i in range(len(l)):
            temp_value = func(temp_value, l[i])
        print("Value is", temp_value)
        return temp_value

    test_list = [1, 5, 3, 4]
    reduce(test_list, add, 1)
    reduce(test_list, multiply, 2)
    reduce(test_list, divide, 2)
    

# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.


#I tried to do a depth first search approach using caching and it was a time complexity disaster. 
# the idea was that there would be a dictioary which held the node pairs for the first traversed path. we would check if a number was prime, decrement it by one if it was, and if not 
# try to find the smallest number we could decrement it to that was not already in the dictionary. if it was already in teh dictionary, and it had taken fewer steps to get there, we would update that node with the new, fewer amount of steps

# Instead, I have implemented a breadth first solution

import sympy

class decrementN: 

    #creating nodes which will hold the decremented value and the number of steps it took to get there
    def __init__(self, m, steps):
        self.m = m
        self.steps = steps


def no_caching(n):

    node_list = []
    node_list.append(decrementN(n, 0))
    visited_numbers = set()

    while (len(node_list) > 0):

        temp_node = node_list.pop(0)
        if (temp_node.m == 1):
            return temp_node.steps

        #this line will add in the n-1 decremented number if it is not already in our set of visited numbers
        if (temp_node.m - 1) not in visited_numbers:
            node_list.append(decrementN(temp_node.m - 1, temp_node.steps +1))

        #this line will loop and add in all of the divisors of m
        for i in range (2, int(temp_node.m // 2)):

            if ((temp_node.m / i) not in visited_numbers and temp_node.m % i == 0):
                node_list.append(decrementN(temp_node.m / i, temp_node.steps + 1))
                visited_numbers.add(temp_node.m / i)

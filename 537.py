# Boggle is a game played on a 4 x 4 grid of letters. 
# The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, 
# using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.



# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

# if n is even, the next number in the sequence is n / 2
# if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

def check(n, success_list):
    visited = []
    if n in success_list: 
        return success_list
    while (n not in success_list and n not in visited):
    
        visited.append(n)
        if (n % 2 == 1):
            # print("n is odd")
            n = 3 * n + 1
        else:
            # print("n is even")
            n = n / 2

        
        if n == 1 or n in success_list:
            print("true")
            # print("success list: ", success_list)
            # print("visited: ", visited)
            success_list.append(n)
            for n in range(len(visited)):
                success_list.append(visited[n])
            print("success list: ", success_list)
            return success_list
        elif n in visited:
            print("false")
            return success_list
 

def check_all(success_list):
    flagged = True
    for n in range(1, 10):
        print(success_list)
        ans = check(n, success_list)
        for n in range(len(ans)):
            print("appending")
            success_list.append(ans[n])
    return True



check_all([])

            

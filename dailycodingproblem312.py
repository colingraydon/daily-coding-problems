# Daily-Coding-Problem-312
#You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

#Dominoes, or 2 x 1 rectangles.
#Trominoes, or L-shapes.
#For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

#A B B C
#A B C C
#Given an integer N, determine in how many ways this task is possible.


#strict recursion is an awful solution here. it's going to spiral in complexity very quickly. I used dynamic programming instead
#I suspect that there is a solution which uses neither but it would take quite a bit of math to come up with

def function(N):
    if (N < 0):
        print("not a valid input")
    if (N < 3):
        return N
 
    dp = [[0] * 3 for _ in range(N + 1)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1
 
    for i in range(2, N+1):
        dp[i][0] = (dp[i-1][0] + dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2])
        dp[i][1] = (dp[i-1][0] + dp[i-1][2])
        dp[i][2] = (dp[i-1][0] + dp[i-1][1])
    return int(dp[N][0])
 
print(function(4))

# You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

# Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

class LexicographicComparision:

    def compare(s, k):

        i = 0
        result = ""
        while (len(s) > 0):
            lowest_char = s[0]
            while (i < k and i < len(s)):
                if (s[i] < lowest_char):
                    lowest_char = s[i]
                i += 1
            result += lowest_char

            for i in range(k):
                if (s[i] == lowest_char):
                    s = s[0:i] + s[i+1:]

        return result




#algo. for the first k elements - check element i against all elements 0 - k. find the lowest char and remove it from the string and add it to a temp string
#continue this process until the input string has no more characters.

#I am not 100% sure this works but it worked for the test cases I did. This will work in O(n^2)

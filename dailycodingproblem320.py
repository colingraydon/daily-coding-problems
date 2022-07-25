#Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.
#the trivial answer here is to use nested for loops, but this will give us O(n^2) time complexity
#i used window sliding instead

#must use defaultdict because i will be checking key value pairs which have not yet been added
from collections import defaultdict

def function(str):

    min_length = string_length = len(str)
    set = {}

    for element in str:
        set.add(element)

    distinct_chars = len(set)

    n = start_index = 0
    count = defaultdict(lambda:0)

    
    for i in range(string_length):
        #this line gets a count of all the unique characters in the whole string and puts it into the dictionary
        count[str[i]] = count[str[i]] + 1
        if count[str] == 1:
            n += 1
        #these lines start sliding the window/start index once we get all the unique chars
        if n == distinct_chars:
            while count[str[start_index]] > 1:
                if count[str[start_index]] > 1:
                    count[str[start_index]] -= 1
                start_index += 1

            #these lines will change the window size
            window_size = i - start_index +1
            if min_length > window_size:
                min_length = window_size
                best_start_index = start_index

        answer = str(str[best_start_index: best_start_index + min_length])
        return answer
            

        
        
    


    


    




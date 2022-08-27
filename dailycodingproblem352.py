# A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

# Every white square must be part of an "across" word and a "down" word.
# No word can be fewer than three letters long.
# Every white square must be reachable from every other white square.
# The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).
# Write a program to determine whether a given matrix qualifies as a crossword grid.

# I am representing black squares as 0s and white squares as 1s

class Crossword:


    def check_reachability(l):

        q = []
        n = len(l)
        result = True
        traversed_map = l
        i,j = 0
        #find the starting space for the first white square
        #this assumes that there is no black square border around the crossword, which is reasonable
        while(l[i][j] == 0):
            i+=1
        #creates a queue of adjacent spaces from the starting point. checks that the space is valid and if it has not been traversed yet. if so, adds it to the queue and marks it as traversed
        #while this queue is not empty, continues this same operation
        q.append([i, j])
        traversed_map[i][j] = 0
        while(len(q) > 0):
            temp = q.pop()
            i = temp[0]
            j= temp[1]
            #check right
            if(Crossword.is_space_valid(l, i+1, j) is True and traversed_map[i+1][j] == 1):
                q.append([i+1,j])
                traversed_map[i+1][j] = 0
            #check left
            if(Crossword.is_space_valid(l, i-1, j) is True and traversed_map[i-1][j] == 1):
                q.append([i-1,j])
                traversed_map[i-1][j] = 0
            #check up
            if(Crossword.is_space_valid(l, i, j+1) is True and traversed_map[i][j+1] == 1):
                q.append([i,j+1])
                traversed_map[i][j+1] = 0
            #check down
            if(Crossword.is_space_valid(l, i, j-1) is True and traversed_map[i][j-1] == 1):
                q.append([i,j-1])
                traversed_map[i][j-1] = 0
        #now that the matrix has been fully traversed, we check the traversed map
        i,j = 0
        while (i < n):
            while(j < n):
                if (traversed_map[i][j] == 1):
                    result = False
                j+= 1
            i +=1
        return result


    def check_symmetry(l):

        symmetric = True
        n = len(l)
        i, j = 0
        while (i < (n / 2)):
            while (j < (n / 2)):
                if (l[i][j] == l[n-i][j] and l[i][j] == l[n-i][n-j] and l[i][j] == l[i][n-j]):
                    symmetric = False
                j+=1
            i+=1
        return symmetric

    #helper method
    def is_space_valid(l, i, j):
        
        result = True
        n = len(l)
        if l[i][j] == 0:
            result = False
        if (i < 0 or j < 0):
            result = False
        if (i >= n or j >= n):
            result = False
        return result
        




    #this method checks that the word length, of any square in the crossword, is 3 or longer
    #it also checks that every white square is part of both a vertical and horizontal word
    def check_word_length(l):

        result = True
        n = len(l)
        i,j = 0
        while (i < n):
            while(j < j):
                if(l[n][j] == 1):
                    temp = 1
                    temp_i = i
                    temp_j = j
                    #check left
                    while(Crossword.is_space_valid(l, temp_i -1, temp_j)):
                        temp_i -= 1
                        temp += 1
                    #check right
                    temp_i = i
                    while(Crossword.is_space_valid(l, temp_i + 1, temp_j)):
                        temp_i += 1
                        temp += 1
                    if ( temp < 3):
                        result = False
                    #check up
                    temp = 1
                    temp_i = i
                    temp_j = j
                    while(Crossword.is_space_valid(l, temp_i, temp_j - 1)):
                        temp_j -= 1
                        temp += 1
                    #check down
                    temp_j = j
                    while(Crossword.is_space_valid(l, temp_i, temp_j +1)):
                        temp_j += 1
                        temp += 1
                    if (temp < 3):
                        result = False
                j+=1
            i+=1
        return result








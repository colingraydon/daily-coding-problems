 #You are given an N by N matrix of random letters and a dictionary of words. 
# Find the maximum number of words that can be packed on the board from the given dictionary.


#I implemented this as a depth first search. This is not efficient but I don't know how to do it faster

class WordCheck:

    #these shouldn't be class variables but i started writing it this way and just never changed it
    word_list = ['eat', 'rain', 'in', 'rat']
    matrix = [['e', 'a', 't'], ['t', 't', 'i'], ['a', 'r', 'a']]
    word_count = 0

    def traverse_matrix(used, temp_string, i, j):

        used[i][j] = True
        temp_string += WordCheck.matrix[i][j]

        #checks if space is valid
        def isSpaceOK(i,j):

            if (i >= 0) and (j >= 0) and (i < len(WordCheck.matrix)) and (j < len(WordCheck.matrix)) and (used[i][j] is False):
                return True
            else:
                return False
        
        if WordCheck.word_in_list(temp_string):
            WordCheck.word_count += 1

        #checks adjacent letters - this problem prompted no diagonals
        if isSpaceOK(WordCheck.matrix[i+1][j]):
            WordCheck.traverse_matrix(used, temp_string, i+1, j)
        if isSpaceOK(WordCheck.matrix[i-1][j]):
            WordCheck.traverse_matrix(used, temp_string, i-1, j)
        if isSpaceOK(WordCheck.matrix[i][j+1]):
            WordCheck.traverse_matrix(used, temp_string, i, j+1)
        if isSpaceOK(WordCheck.matrix[i][j-1]):
            WordCheck.traverse_matrix(used, temp_string, i, j-1)
        
        used[i][j] = False
        #clears last char
        temp_string = temp_string[0:len(temp_string)]
    

    def start_traversal_at_point(i,j):

        #initializes matrix and string for starting at a new point, i j
        temp_string = ""
        used = []
        for i in range(len(WordCheck.matrix)):
            for j in range(len(WordCheck.matrix)):
                used[i][j] is False

        for i in range(len(WordCheck.matrix)):
            for j in range(len(WordCheck.matrix)):
                WordCheck.traverse_matrix(used, temp_string, i,j)
        

    
    def word_in_list(s):

        if s in WordCheck.word_list:
            return True
        else:
            return False

# You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:

#       x
#       x  
#   x   x
#   x x x
# x x x x
# Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.

class histogram():

    def calculate_largest(l):

        ordered_list = []
        max = 0
        i = 0
        while (i < len(l)):

            #adds the height to the stack if it is greater than the current greatest height
            if (len(ordered_list) == 0) or (l[ordered_list[-1]] <= ordered_list[i]):
                ordered_list.append(i)
                i+=1
            #if it is not greater than the current greatest height, we use this element as the right index and the previous lowest as the left index to find area
            else:
                temp_height = ordered_list.pop()
                temp_width = i - ordered_list[-1] - 1
                temp_area = temp_width * l[temp_height]
                if (temp_area > max):
                    max = temp_area

        while (len(ordered_list) > 0):

            temp_height = ordered_list.pop()
            temp_width = i - ordered_list[-1] - 1
            temp_area = l[ordered_list] * temp_width
            if (temp_area > max):
                max = temp_area
        
        return max
            
            


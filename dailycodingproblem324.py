#Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

#I thought about this and I can't think of a scenario where it wouldn't be optimal to just sort the lists and create a 1-1 map from the first list to the last.
#This seems too obvious but I really can't think of a counterexample
#for



#Didn't use a dictionary because mouse positions can be repeated
class mouse:

    def __init__(self, mouse, hole):

        self.mouse = mouse
        self.hole = hole

def mice_to_holes(mice_list, hole_list):

    mice_list.sort()
    hole_list.sort()
    mice_map = []


        
    for i in range(len(mice_list)):

        mice_map.append(mouse(mice_list[1], hole_list[i]))
        print(mice_list[i])
        print(hole_list[i])
    

    return mice_map


    

    



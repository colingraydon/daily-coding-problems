# Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

# On the ith jump, you may move exactly i places to the left or right.

# Find a path with the fewest number of jumps required to get from 0 to N.

#this looks like a breadth first search.
#if i wanted to store the entire path, one way to do it would be to store the previous position, before arriving at n, info (steps and position) in a list.
#then recursively call the jump function on that position, making sure that both the number of steps needed and the position must be correct.
class hopper:

    def __init__(self, position, steps):
        self.position = position
        self.steps = steps
    
def jump(n):

        
    position_list = []
    position_list.append(hopper(0, 0))

    while len(position_list) > 0:

        temp_position = position_list.pop(0)
        if (temp_position.position == n):
            return temp_position.steps - 1

        else:
            position_list.append(hopper(temp_position.position + temp_position.steps, temp_position.steps + 1))
            position_list.append(hopper(temp_position.position - temp_position.steps, temp_position.steps + 1))



print(jump(2))



#You are the technical director of WSPT radio, serving listeners nationwide
#For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).
#Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, 
# determine what the minimum broadcast range would have to be in order for each listener's home to be covered.
#For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]
#In this case the minimum range would be 5, since that would be required for the tower at position 15 to reach the listener at position 20.

#for this solution, you can leave the lists as lists without converting to arrays, it isn't necessary. I'm just trying to use numpy more

import numpy as np
def function(n,m):
    n.sort()
    m.sort()
    listeners = np.array(n)
    towers = np.array(m)
    min = abs(listeners[0] - towers[0])
    i,j = 0
    while (i < len(listeners) and j < len(towers)):
        min = max(min, abs(listeners[i] - towers[j]))
        if ((listeners[i] < towers[j]) or j == (len(towers) - 1)): 
            i+=1
        else: 
            j+=1
    return min
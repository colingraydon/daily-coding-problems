#You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

#Determine how many times you would need to apply this operation to ensure that all x's come before all y's.

#Dynamic programming should also work for this problem

def flip_letters(data):

    #these 2 dictionaries map the characters index to the number of x's on the right or y's on the left
    x_right_map = {}
    y_left_map = {}
    length = len(data)
    x_count = 0
    y_count = 0

    i = 0
    while (i < length):
        y_left_map[i] = y_count
        if (data[i] == "y"):
            y_count += 1
        i += 1

    i = length - 1

    while (i >= 0):
        x_right_map[i] = x_count
        if (data[i] == "x"):
            x_count += 1
        i -= 1

    for i in x_right_map:
        print("index is ", i, "x to the right are", x_right_map[i])
    
    print("Doing y_left_map now")

    for i in y_left_map:
        print("index is ", i, "y to the left are", y_left_map[i])


    i = 0
    least_flips = x_right_map[i] + y_left_map[i]

    #The number of flips required, at any index, would be teh flips needed of ys on the left plus flips of x to the right. The values of the dictionaries, for key index = i, are added together
    while (i < length):
        temp_flip_number = x_right_map[i] + y_left_map[i]
        if (temp_flip_number < least_flips):
            least_flips = temp_flip_number
        i += 1
    
    print("least_flips is" , least_flips)
    return least_flips
    
y =flip_letters("xyxxxyxyy")
print(y)
    
    
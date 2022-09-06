#A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

#Create a program that finds all strobogrammatic numbers with N digits.

#relevant digits are 0,1,8, and 6/9 if on opposite ends
def find_strobogrammatic(n):

    if (n == 0):
        return []
    if (n == 1):
        return ["0", "1", "8"]

    temp = find_strobogrammatic(n - 2)
    result = []

    for element in temp:
        result.append("0" + element + "0")
        result.append("1" + element + "1")
        result.append("6" + element + "9")
        result.append("8" + element + "8")
        result.append("9" + element + "6")

    return result


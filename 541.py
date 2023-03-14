# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. 
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

def encode(input):

    output = ""
    n = 0
    length = len(input)
    consecutive = []

    while (n < length):
        temp_char = input[n]
        if (len(consecutive) == 0) or (consecutive[len(consecutive) - 1] == temp_char):
            consecutive.append(temp_char)
            if (n == length - 1):
                digit = str(len(consecutive))
                char = consecutive[len(consecutive) - 1]
                output = output + digit + char

        else:
            digit = str(len(consecutive))
            char = consecutive[len(consecutive) - 1]
            output = output + digit + char
            consecutive = []
            consecutive.append(temp_char)
        n += 1
        
    print(output)


def decode(input):
    output = ""
    index = 0
    while (index < len(input)):
        if (index % 2 == 0):
            digit = int(input[index])
        else:
            char = input[index]
            counter = 0
            while (counter < digit):
                output += char
                counter += 1
        index += 1

    print(output)

encode("AAAABBBCCDAA")

decode("4A3B2C1D2A")



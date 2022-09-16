# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Write a function that takes a natural number as input and returns the number of digits the input has.

# Constraint: don't use any loops.




digits = 1

def get_digits(n):

    global digits
    if ((n/10) < 1):

        print(digits)

    else:

        digits += 1
        get_digits(n / 10)


get_digits(5010)
    

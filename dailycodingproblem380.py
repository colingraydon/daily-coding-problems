# Implement integer division without using the division operator. Your function should return a tuple of (dividend, remainder) and it should take two numbers, the product and divisor.

# For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.

def division(a, b):

    ans = 0 
    temp = a
    while (temp > 0):

        temp = temp - b
        ans += 1

    quotient = temp + b
    if (quotient == b):
        quotient = 0
        ans += 1
    answer = []
    answer.append(ans -1)
    answer.append(quotient)

    return answer

print(division(15,9))
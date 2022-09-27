
#Implement a function that converts a hex string to base64.

def base10to64(n):

    charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+='
    result = ''
    while (n > 0):

        temp = n%64
        result = charset[temp] + result
        n = n // 64
    print(result)

base10to64(102348239481)

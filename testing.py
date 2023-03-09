def fib(n):

    s = [1, 1]

    while (len(s) < n):
        s.append(s[-1] + s[-2])
    return s[-1]

print(fib(6))
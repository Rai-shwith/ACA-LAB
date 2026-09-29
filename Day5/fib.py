# How can we calculate the nth Fibonacci number using recursion?
def fib(n):
    if n <=1 :
        return n

    return fib(n-1) + fib(n-2)

while True:
    num = int(input("Enter the number : "))
    print(fib(num))

"""
1. Return n directly when n is 0 or 1, because these are the base cases.
2. Otherwise recursively calculate fib(n - 1) and fib(n - 2).
3. Add the two recursive results and return the sum.
"""
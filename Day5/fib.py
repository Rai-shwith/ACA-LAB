# Fibanocci of n terms using recursion
def fib(n):
    if n <=1 :
        return n

    return fib(n-1) + fib(n-2)

while True:
    num = int(input("Enter the number : "))
    print(fib(num))
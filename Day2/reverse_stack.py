def reverse_stack(stack1):
    stack2 = []
    while stack1:
       stack2.append(stack1.pop())
    return stack2


while True:
    arr = list(map(int,input("Enter the elements by leaving space(eg: 1 2 3):\n").split()))
    if not arr:
        print("Bye Bye!")
        break
    print(reverse_stack(arr))
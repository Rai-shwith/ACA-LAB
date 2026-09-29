# How can we reverse a stack using an auxiliary stack?
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
    
"""
python reverse_stack.py 
Enter the elements by leaving space(eg: 1 2 3):
3 4 5 6 7 8
[8, 7, 6, 5, 4, 3]
Enter the elements by leaving space(eg: 1 2 3):
1 -1 2 3 4
[4, 3, 2, -1, 1]
Enter the elements by leaving space(eg: 1 2 3):

Bye Bye!
"""

"""
1. Create an empty auxiliary stack.
2. Pop each element from the input stack and push it onto the auxiliary stack.
3. Return the auxiliary stack after the input stack is empty.
"""
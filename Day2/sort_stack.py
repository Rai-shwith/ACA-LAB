def sort_stack(stack1):
    stack2 = []
    
    while stack1 :
        ele1 = stack1.pop()
        
        while stack2 and  ele1 < stack2[-1]:
            ele2 = stack2.pop()
            stack1.append(ele2)
        
        stack2.append(ele1)
        
            
    return stack2

while True:
    arr = list(map(int,input("Enter the elements by leaving space(eg: 1 2 3):\n").split()))
    if not arr:
        print("Bye Bye!")
        break
    print(sort_stack(arr))

"""
 python sort_stack.py 
Enter the elements by leaving space(eg: 1 2 3):
1 -2 2 3 4 0 -1 -3
[-3, -2, -1, 0, 1, 2, 3, 4]
Enter the elements by leaving space(eg: 1 2 3):
0 1 2 3 4 
[0, 1, 2, 3, 4]
Enter the elements by leaving space(eg: 1 2 3):
4 3 2 1 
[1, 2, 3, 4]
Enter the elements by leaving space(eg: 1 2 3):

Bye Bye!
"""
    

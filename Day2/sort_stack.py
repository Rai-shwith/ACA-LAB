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
    

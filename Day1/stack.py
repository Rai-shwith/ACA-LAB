from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
        
    def push(self,ele):
        print(f"pushing {ele}")
        self.q2.append(ele)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.q1:
            ele =  self.q1.popleft()
            print(f"Popped {ele}")
        else:
            print("Empty Stack")

    
s = Stack()

while True:
    exp = input("Enter \n'1' for Push \n'2' for Pop \n'q' for quitting: ")
    if exp == "1":
        ele = input("Enter Element: ")
        s.push(ele)
    elif exp == "2":
        s.pop()
    elif exp == "q":
        break
    else:
        print("Invalid input")

    
    
"""
python stack.py 
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 1
Enter Element: 2
pushing 2
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 1
Enter Element: 5
pushing 5
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 1
Enter Element: 10
pushing 10
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 2
Popped 10
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 2
Popped 5
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 2
Popped 2
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 2
Empty Stack
Enter 
'1' for Push 
'2' for Pop 
'q' for quitting: 
"""
def check(expression):
    stack = []
    charMap = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for i in expression:
        if i not in "()[]{}":
            continue
        
        if i not in charMap:
            stack.append(i)
        elif not stack or  stack.pop() != charMap[i]:
            print("INVALID!!!!")
            return
    if not stack:
        print("PASSED")
    else:
        print("INVALID !!!")
            

print("Welcome for Expression Validator! \nPress q to quit")
while True:
    exp = input("Enter the Expression: ")
    
    if exp == "q":
        break
    check(exp)
    
    
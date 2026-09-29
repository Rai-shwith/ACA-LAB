# How can we determine whether an array represents a min-heap or max-heap?
def is_heap(arr,isMin):
    n = len(arr)
    for i in range((n//2-1),-1,-1):
        minValid = min(arr[i],arr[2*i+1],arr[2*i+2]) == arr[i]
        if (isMin and not minValid) or (not isMin and minValid):
            return False
    return True

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    isMin = input("Are you checking for Min heap? [y/n]: ").lower() == "y"
    if is_heap(nums,isMin):
        print("Its a Heap")
    else:
        print("Nah, dude its not heap")

"""
1. Start at the last internal node and move backward toward the root.
2. Compare each node with its two children to determine whether the required heap relation holds.
3. Return False immediately when a node violates the selected min-heap or max-heap rule.
4. Return True after every internal node passes the check.
"""

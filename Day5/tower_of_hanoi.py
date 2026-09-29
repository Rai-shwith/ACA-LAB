# How can we solve the Tower of Hanoi problem recursively?
def TowerOfHanoi(n, fromRod, toRod, auxRod):
    if n == 0:
        return
    TowerOfHanoi(n-1, fromRod, auxRod, toRod)
    print("Disk", n, " moved from ", fromRod, " to ", toRod)
    TowerOfHanoi(n-1, auxRod, toRod, fromRod)

while True:
    n = int(input("Enter the number of disks: "))
    
    # A, C, B are the name of rods
    TowerOfHanoi(n, 'A', 'C', 'B ')
    
    
a ,c
a, b
b, c

"""
1. Return when there are no disks to move.
2. Recursively move the top n - 1 disks from the source rod to the auxiliary rod.
3. Move the largest disk from the source rod to the destination rod.
4. Recursively move the n - 1 disks from the auxiliary rod to the destination rod.
"""
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
# Sum of all the elements to 
def sum_to_n(n,arr):
    if n == 0 :
        return 0

    return arr[n-1] + sum_to_n(n-1,arr)

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    print(sum_to_n(len(nums),nums))
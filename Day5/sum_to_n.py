# How can we recursively sum all elements in an array?
def sum_to_n(n,arr):
    if n == 0 :
        return 0

    return arr[n-1] + sum_to_n(n-1,arr)

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    print(sum_to_n(len(nums),nums))

"""
1. Return 0 when the number of elements to process is zero.
2. Add the last unprocessed element to the recursive sum of the preceding elements.
3. Continue until the base case is reached, then return the total.
"""
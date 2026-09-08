# Write a program to find kth largest element using heap
import heapq
def largest_kth_element(arr,k):
    heapq.heapify(arr)
    while len(arr) > k:
        heapq.heappop(arr)
    return heapq.heappop(arr)


arr = list(map(int,input("Enter the array elements (eg: 1 2 3 ): ").split()))
k = int(input("Enter k: "))
print(f"Kth Largest Element :",largest_kth_element(arr,k))

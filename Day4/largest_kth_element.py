# How can we find the kth largest element using a heap?
import heapq
def largest_kth_element(arr,k):
    heapq.heapify(arr)
    while len(arr) > k:
        heapq.heappop(arr)
    return heapq.heappop(arr)


arr = list(map(int,input("Enter the array elements (eg: 1 2 3 ): ").split()))
k = int(input("Enter k: "))
print(f"Kth Largest Element :",largest_kth_element(arr,k))

"""
1. Convert the input array into a min-heap.
2. Remove the smallest element until only the k largest elements remain.
3. Remove and return the root of the heap, which is the kth largest element.
"""

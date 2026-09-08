# Write a program to demonstrate heap sort using heap data structure
class Heap:
    def __init__(self, arr=[]):
        self.n = len(arr)
        self.arr = arr
        self.heapify()

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        

    def sink(self, i):
        # Helper to maintain min-heap property down the tree from index i
        while 2 * i + 1 < self.n:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < self.n and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < self.n and self.arr[right] < self.arr[smallest]:
                smallest = right

            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def heapify(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.sink(i)

    def heappop(self):
        if self.n == 0:
            return
        self.swap(0, self.n - 1)
        ans = self.arr.pop()
        self.n -= 1
        if self.n > 0:
            self.heapify()
        return ans
        

    def heapsort(self):
        backup_heap = self.arr.copy()
        backup_n = self.n
        sorted_arr = []
        while self.n != 0:
            sorted_arr.append(self.heappop())
        self.arr = backup_heap
        self.n = backup_n
        return sorted_arr

arr = map(int,input("Enter the array elements (eg: 1 2 3 ): ").split())
h = Heap(list(arr))
print(f"Sorted Array: ", h.heapsort())


"""
$ python heap_sort.py 
Enter the array elements (eg: 1 2 3 ): 1 -4 20 9 8 
Sorted Array:  [-4, 1, 8, 9, 20]
"""
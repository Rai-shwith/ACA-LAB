from Day4.heap_sort import Heap

def print_less_than_x(heap,x):
    while (val:= heap.heappop()) < x:
        print(val)

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    x = int(input("Enter X: "))
    heap = Heap(nums)
    print_less_than_x(heap,x)
    
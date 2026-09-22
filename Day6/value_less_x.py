from Day4.heap_sort import Heap

def print_less_than_x(heap,x):
    while (val:= heap.heappop()) < x:
        print(val)

def dfs(heap,i,x):
    if i < len(heap) and  heap[i] < x:
        print(heap[i])
    else:
        return
    l = 2*i + 1
    r = 2*i + 2
    dfs(heap,l,x)
    dfs(heap,r,x)

while True:
    nums = list(map(int,input("Enter the numbers eg: 1 2 3 : ").split()))
    x = int(input("Enter X: "))
    heap = Heap(nums)
    dfs(heap,0,x)
    
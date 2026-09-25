class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    if not head:
        return None
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False        


def create_linked_list(arr,idx):
    dummy = Node(-1)
    cur = dummy
    for ele in arr:
        node = Node(ele)
        cur.next = node
        cur = cur.next

    if idx != -1:
        temp = dummy
        for _ in range(idx):
            temp = temp.next
    
        cur.next = temp
    return dummy.next

arr = list(map(int,input("Enter the array, eg: (1 2 3): ").split()))
cycle_position = int(input("Enter the index to create cycle, give -1 to skip the cycle: "))

head = create_linked_list(arr,cycle_position)
if detect_cycle(head):
    print("Bro, It has cycle")
else:
    print("No cycle, dude!")
# How can we find the middle node of a singly linked list?
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def find_middle(head):
    if not head:
        return None
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow        


def create_linked_list(arr):
    dummy = Node(-1)
    cur = dummy
    for ele in arr:
        node = Node(ele)
        cur.next = node
        cur = cur.next
        
    return dummy.next

arr = list(map(int,input("Enter the array, eg: (1 2 3): ").split()))

head = create_linked_list(arr)
middle = find_middle(head)
if middle:
    print(f"Middle element is {middle.val}")
else:
    print("No middle element found.")

"""
1. Return None for an empty list.
2. Move a slow pointer one node at a time and a fast pointer two nodes at a time.
3. When the fast pointer reaches the end, the slow pointer is at the middle.
4. Return the slow pointer.
"""
class Node:
    def __init__(self,data=0,nxt=None):
        self.val = data
        self.next = nxt


# Helper function 
def create_ll(arr):
    dummy = Node()
    cur = dummy
    for i in arr:
        node = Node(i)
        cur.next = node
        cur = node
    return dummy.next

def reverse_ll(head):
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

def print_ll(head):
    cur = head
    if cur:
        print(cur.val,end="")

    cur = cur.next
    while cur:
        print("->",cur.val,end="")
        cur = cur.next
    print()



while True:
    arr = list(map(int,input("Enter the LL elements (eg: 1 2 3 4): ").split()))
    if not arr:
        print("Bye Bye!!")
        break
    head = create_ll(arr)
    print("Current LL: ")
    print_ll(head)
    head = reverse_ll(head)
    print("After Reversal : ")
    print_ll(head)

"""
@Rai-shwith ➜ /workspaces/ACA-LAB/Day3 (main) $ python reverse_ll.py 
Enter the LL elements (eg: 1 2 3 4):  1 2 5 8 9
Current LL: 
1-> 2-> 5-> 8-> 9
After Reversal : 
9-> 8-> 5-> 2-> 1
Enter the LL elements (eg: 1 2 3 4): 
Bye Bye!!
"""
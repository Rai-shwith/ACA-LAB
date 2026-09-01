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

def merge_two_ll(h1,h2):
    dummy_head = Node()
    dummy = dummy_head
    c1,c2 = h1,h2
    while c1 and c2:
        if c1.val < c2.val:
            dummy.next = c1
            c1 = c1.next
        else:
            dummy.next = c2
            c2 = c2.next
        dummy = dummy.next

    while c1:
        dummy.next = c1
        c1 = c1.next
        dummy = dummy.next
        
    while c2:
        dummy.next = c2
        c2 = c2.next
        dummy = dummy.next

    return dummy_head.next


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
    arr1 = list(map(int,input("Enter the First sorted LL  elements (eg: 1 2 3 4): ").split()))
    arr2 = list(map(int,input("Enter the Second sorted LL elements (eg: 1 2 3 4): ").split()))
    if not arr1 or not arr2:
        print("Bye Bye!!")
        break
    h1 = create_ll(arr1)
    h2 = create_ll(arr2)
    print("Current LL 1: ")
    print_ll(h1)
    print("Current LL 2: ")
    print_ll(h2)
    m = merge_two_ll(h1,h2)
    print("After merging : ")
    print_ll(m)
    
"""

@Rai-shwith ➜ /workspaces/ACA-LAB/Day3 (main) $ python merge_two_ll.py 
Enter the First sorted LL  elements (eg: 1 2 3 4): 1 3 5 7 10
Enter the Second sorted LL elements (eg: 1 2 3 4): 2 4 6 8 10 11 12
Current LL 1: 
1-> 3-> 5-> 7-> 10
Current LL 2: 
2-> 4-> 6-> 8-> 10-> 11-> 12
After merging : 
1-> 2-> 3-> 4-> 5-> 6-> 7-> 8-> 10-> 10-> 11-> 12
Enter the First sorted LL  elements (eg: 1 2 3 4): 
Enter the Second sorted LL elements (eg: 1 2 3 4): 
Bye Bye!!
"""
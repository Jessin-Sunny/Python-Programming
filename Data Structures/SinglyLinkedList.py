# defining class Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# insert element x at begining
def insert_front(head, x):
    newNode = Node(x)
    if head is None:
        return newNode
    newNode.next = head
    return newNode

# insert element x at the end
def insert_end(head, x):
    newNode = Node(x)
    if head is None:
        return newNode
    current = head
    while current.next is not None:
        current = current.next
    current.next = newNode
    return head

# insert at specific position
def insert_position(head, x, pos):
    if pos < 1:
        return head
    newNode = Node(x)
    if head is None:
        return newNode
    if pos == 1:
        newNode.next = head
        return newNode
    
    current = head
    # just before node
    for i in range(1, pos - 1):
        if current is None:
            return head
        current = current.next
    newNode.next = current.next
    current.next = newNode
    return head

# delete head node and return new head
def delete_front(head):
    if head is None:
        print("Empty")
        return None
    head = head.next
    print("Deleted Successfully")
    return head

def delete_end(head):
    if head is None:
        print("Empty")
        return None
    if head.next is None:
        return None
    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next
    secondLast.next = None
    print("Deleted Successfully")
    return head

def delete_position(head, pos):
    temp = head
    if head is None:
        print("Empty")
        return None
    if pos == 1:
        head = head.next
    prev = None
    for i in range(1, pos):
        prev = temp
        temp = temp.next

    prev.next = temp.next
    print("Deleted Successfully")
    return head
# print linked list
def print_list(head):
    if head is None:
        print("Empty")
    current = head
    while current is not None:
        if current.next is None:
            print(current.data)
            break
        print(current.data, end="->")
        current = current.next

head = None
while True:
    print("1 : INSERTION")
    print("2 : DELETION")
    print("3 : PRINTING")
    print("4 : EXIT")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        n = int(input("How many elements ? : "))
        for i in range(n):
            print("1 : FRONT")
            print("2 : END")
            print("3 : POSITION")
            i = int(input())
            print("Enter the element")
            a = int(input())
            if i == 1:
                head = insert_front(head, a)
            elif i == 2:
                head = insert_end(head, a)
            elif i == 3:
                p = int(input("Enter the position : "))
                head = insert_position(head, a, p)
            else:
                print("Invalid Choice")
    elif ch == 2:
        print("1 : FRONT")
        print("2 : END")
        print("3 : POSITION")
        i = int(input())
        if i == 1:
            head = delete_front(head)
        elif i == 2:
            head = delete_end(head)
        elif i == 3:
            p = int(input("Enter the position : "))
            head = delete_position(head, p)
        else:
            print("Invalid Choice")
    elif ch == 3:
        print_list(head)
    elif ch == 4:
        break
    else:
        print("Invalid Choice")

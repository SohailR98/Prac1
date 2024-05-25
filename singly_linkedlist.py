class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def traverse(head):
    current = head
    while current:
        print(current.data, end = " -> ")
        current = current.next

    print("None")


def insert_after_node(node, data):
    if node is None:
        print("Error: the given node is none")
        return
    
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def deletion_at_beginning(head):

    if head is None:
        print("LL is empty")
        return None
    new_head = head.next
    del head
    return new_head

def deletion_at_end(head):
    if head is None or head.next is None:
        print("Either the list is empty or it has only one node")
        return None
    
    current = head
    while current.next.next:
        current = current.next

    del_node = current.next
    current.next = None
    del del_node

    return head





head = None
head = insert_at_beginning(head, 1)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 4)
insert_after_node(head ,5)
insert_at_end(head, 10)
print("list before deletion")
traverse(head)

head = deletion_at_beginning(head)
head = deletion_at_end(head)
print("list after deletion")
traverse(head)
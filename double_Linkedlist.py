class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend (self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev

                if current == self.head:
                    self.head = current.next

                current = None

                return
            current = current.next 

    def print_list(self):
        current=self.head

        while current:
            print(current.data, end = "<->")
            current = current.next
        print("None")


dll = DoublyLinkedList()
dll.append(1)            
dll.append(2)            
dll.append(3)            
dll.append(4)
print("Full dll")
dll.print_list()            

print("after prepend")
dll.prepend(6)
dll.prepend(7)
dll.prepend(8)
dll.prepend(9)
dll.print_list()

print("after deletion")
dll.delete(8)
dll.print_list()
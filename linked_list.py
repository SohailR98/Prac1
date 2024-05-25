class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def deleteN(self, position):
        if self.head is None:
            return

        temp = self.head
        prev = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position):
            prev = temp
            temp = temp.next

            if temp is None:
                break

        if temp is not None:
            prev.next = temp.next
            temp = None




    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")



linked_list = Linkedlist()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)


linked_list.print_list()

print("linked list after adding new elements")

linked_list.push(4)
linked_list.push(5)
linked_list.push(6)
linked_list.print_list()

print("deletion of 1st element")

linked_list.deleteN(0)
linked_list.print_list()


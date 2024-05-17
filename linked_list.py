class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class Linkedlist:

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

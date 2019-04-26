from .Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current.data))
            current = current.next
        return '[' + ' -> '.join(nodes) + ']'

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        if self.head:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = Node(data)

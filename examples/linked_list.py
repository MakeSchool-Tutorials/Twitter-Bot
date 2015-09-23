class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            last_node = self.last()
            last_node.next = node
        return node

    def all(self):
        all = []
        current = self.head
        while current:
            all.append(current)
            current = current.next
        return all

    def count(self):
        count = 0
        def count_up(node):
            nonlocal count
            count += 1
        self.walk(count_up)
        return count

    def find(self, func):
        current = self.head
        while current:
            if func(current) == True:
                return current
            current = current.next
        return None

    def walk(self, func):
        current = self.head
        while current:
            func(current)
            current = current.next
        return self

    def last(self):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = node
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return node

    def delete(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.prev.next = node.next
        node.next.prev = node.prev

    def all(self):
        all = []
        current = self.head
        while current:
            all.append(current)
            current = current.next
        return all

    def count(self):
        nonlocal count
        count = 0
        def count_up(node):
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

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

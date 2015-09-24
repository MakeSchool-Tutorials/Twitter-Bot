class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return node

    def delete(self, data):
        previous = None
        current = self.head
        while current:
            if current.value != data:
                previous = current
                current = current.next
                continue

            if self.head == current:
                self.head = current.next
            if self.tail == current:
                self.tail = previous
            if previous:
                previous.next = current.next
            return self
        return None

    def insert(self, data, prevNode):
        newNode = Node(data)
        if self.tail == prevNode:
            self.tail = newNode
        else:
            newNode.next = prevNode.next
        prevNode.next = newNode

    def find(self, func):
        current = self.head
        while current:
            if func(current.value) == True:
                return current.value
            current = current.next
        return None

    def findNode(self, func):
        current = self.head
        while current:
            if func(current) == True:
                return current
            current = current.next
        return None

    def all(self):
        all = []
        current = self.head
        while current:
            all.append(current.value)
            current = current.next
        return all

    def count(self):
        count = 0
        def count_up(node):
            nonlocal count
            count += 1
        self.walk(count_up)
        return count

    def walk(self, func):
        current = self.head
        while current:
            func(current)
            current = current.next
        return self

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

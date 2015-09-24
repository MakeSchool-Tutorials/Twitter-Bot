# features:
# - create new hash table
# - set key to value
# - update key value
# - get value for key
# - get list of keys
# - get list of values
# - convert to list of tuples
from linked_list import *

class HashTable:
    def __init__(self, num_buckets=None):
        if num_buckets == None:
            num_buckets = 2 ** 3
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for i in range(num_buckets)]

    def __setitem__(self, key, value):
        return self.set(key, value)

    def set(self, key, value):
        list = self.buckets[self.index(key)]
        item = (key, value)
        list.append(item)
        return item

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        pair = self.find(key)
        return pair and pair[-1]

    def update(self, key, value):
        list = self.buckets[self.index(key)]
        def updateNode(node):
            if node.value[0] == key:
                node.value = (key, value)
        list.walk(updateNode)
        return self

    def keys(self):
        return [data[0] for list in self.buckets for data in list.all()]

    def values(self):
        return [data[1] for list in self.buckets for data in list.all()]

    def to_list(self):
        return [data for list in self.buckets for data in list.all()]

    def count(self):
        total = 0
        for listcount in [list.count() for list in self.buckets]:
            total += listcount
        return total

    def find(self, key):
        list = self.buckets[self.index(key)]
        return list.find(self.is_same_key(key))

    def is_same_key(self, key):
        def same_key(data):
            return data[0] == key
        return same_key

    def index(self, key):
        return hash(key) % self.num_buckets

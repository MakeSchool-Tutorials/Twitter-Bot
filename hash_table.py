# features:
# - create new hash table
# - set key to value
# - update key value
# - get value for key
# - get list of keys
# - get list of values
# - convert to list of tuples

class HashTable:
    def __init__(self):
        self.table = []

    def set(self, key, value):
        new_item = (hash(key), key, value)
        insert_before_index = self.insert_index(new_item)
        self.table.insert(insert_before_index, new_item)
        return self.table

    def get(self, key):
        hashkey = hash(key)
        index = self.get_index(hashkey)
        if index == None:
            return None
        item = self.table[index]
        return item[-1]

    def update(self, key, value):
        hashkey = hash(key)
        index = self.get_index(hashkey)
        if index == None:
            raise Exception('Key not found.')
        updated_item = (hashkey, key, value)
        self.table[index] = updated_item
        return updated_item

    def keys(self):
        return [item[1] for item in self.table]

    def values(self):
        return [item[-1] for item in self.table]

    def to_list(self):
        return [(item[1], item[-1]) for item in self.table]

    def insert_index(self, new_item):
        insert_index = 0
        size = len(self.table)
        for idx, item in enumerate(self.table):
            if idx == 0 and item[0] > new_item[0]:
                insert_index = idx
                break
            elif idx < size and self.is_between(new_item[0], self.table[idx - 1][0], item[0]):
                insert_index = idx
                break
            elif idx == size - 1 and item[0] < new_item[0]:
                insert_index = size
                break
        return insert_index

    def is_between(self, item, first, second):
        return item > first and item < second

    def get_index(self, hashkey, table=None, offset=None):
        if table == None:
            table = self.table
        if offset == None:
            offset = 0
        size = len(table)
        if size == 0:
            return None
        mid_index = size // 2
        mid_item = table[mid_index]
        if hashkey == mid_item[0]:
            return offset + mid_index
        elif hashkey < mid_item[0]:
            return self.get_index(hashkey, table[0:mid_index], offset)
        else:
            offset = offset + mid_index + 1
            return self.get_index(hashkey, table[mid_index + 1:], offset)

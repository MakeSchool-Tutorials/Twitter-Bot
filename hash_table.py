# features:
# - create new hash table
# - insert key value
# - update key value
# - get value for key
# - get list of keys
# - get list of values
# - convert to list of tuples

def create():
    return [];

def insert(key, value, hashtbl):
    new_item = (hash(key), key, value)
    insert_before_index = insert_index(new_item, hashtbl)
    hashtbl.insert(insert_before_index, new_item)
    return hashtbl

def get(key, hashtbl):
    hashkey = hash(key)
    index = get_index(hashkey, hashtbl)
    if index == None:
        return None
    item = hashtbl[index]
    return item[-1]

def update(key, value, hashtbl):
    hashkey = hash(key)
    index = get_index(hashkey, hashtbl)
    if index == None:
        raise Exception('Key not found.')
    updated_item = (hashkey, key, value)
    hashtbl[index] = updated_item
    return updated_item

def keys(hashtbl):
    return [item[1] for item in hashtbl]

def values(hashtbl):
    return [item[-1] for item in hashtbl]

def to_list(hashtbl):
    return [(item[1], item[-1]) for item in hashtbl]

def insert_index(new_item, hashtbl):
    insert_index = 0
    size = len(hashtbl)
    for idx, item in enumerate(hashtbl):
        if idx == 0 and item[0] > new_item[0]:
            insert_index = idx
            break
        elif idx < size and is_between(new_item[0], hashtbl[idx - 1][0], item[0]):
            insert_index = idx
            break
        elif idx == size - 1 and item[0] < new_item[0]:
            insert_index = size
            break
    return insert_index

def is_between(item, first, second):
    return item > first and item < second

def get_index(hashkey, hashtbl, offset=None):
    if offset == None:
        offset = 0
    size = len(hashtbl)
    if size == 0:
        return None
    mid_index = size // 2
    mid_item = hashtbl[mid_index]
    if hashkey == mid_item[0]:
        return offset + mid_index
    elif hashkey < mid_item[0]:
        return get_index(hashkey, hashtbl[0:mid_index], offset)
    else:
        offset = offset + mid_index + 1
        return get_index(hashkey, hashtbl[mid_index + 1:], offset)

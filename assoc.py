def get(key, assoc_array):
    value = None
    for index, item in enumerate(assoc_array):
        if item == key:
            value = assoc_array[index + 1]
            break
    return value

basic_table = ['I', 1, 'V', 5, 'X', 10]

print(get('V', basic_table))

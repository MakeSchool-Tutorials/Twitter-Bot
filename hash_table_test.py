from hash_table import HashTable

def test():
    htb = HashTable()

    htb.insert('I', 1)
    htb.insert('V', 5)
    htb.insert('X', 10)
    htb.insert('L', 50)
    htb.insert('C', 100)
    htb.insert('D', 500)
    htb.insert('M', 1000)

    print(sorted(htb.table) == htb.table)

    if htb.get('I') != 1:
        print(htb.get('I'))
        print(hash('I'))
        print(htb.table)

    print(htb.get('I') == 1)
    print(htb.get('V') == 5)
    print(htb.get('X') == 10)
    print(htb.get('L') == 50)
    print(htb.get('C') == 100)
    print(htb.get('D') == 500)
    print(htb.get('M') == 1000)
    print(htb.get('foo') == None)

    htb.update('V', 2)

    print(htb.get('V') == 2)

    # print(htb.keys())
    # print(htb.values())
    #
    # print(htb.table)
    # print(htb.to_list())

test()

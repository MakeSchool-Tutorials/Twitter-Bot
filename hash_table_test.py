import hash_table as htb

def test():
    htbl = htb.create()

    htb.insert('I', 1, htbl)
    htb.insert('V', 5, htbl)
    htb.insert('X', 10, htbl)
    htb.insert('L', 50, htbl)
    htb.insert('C', 100, htbl)
    htb.insert('D', 500, htbl)
    htb.insert('M', 1000, htbl)

    print(sorted(htbl) == htbl)

    if htb.get('I', htbl) != 1:
        print(htb.get('I', htbl))
        print(hash('I'))
        print(htbl)

    print(htb.get('I', htbl) == 1)
    print(htb.get('C', htbl) == 100)
    print(htb.get('foo', htbl) == None)

    htb.update('V', 2, htbl)

    print(htb.get('V', htbl) == 2)

    print(htb.keys(htbl))
    print(htb.values(htbl))

    print(htbl)
    print(htb.to_list(htbl))

test()

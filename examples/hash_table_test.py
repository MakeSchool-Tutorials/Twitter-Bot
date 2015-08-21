from hash_table import HashTable

def test():
    htb = HashTable()

    htb.set('I', 1)
    htb.set('V', 5)
    htb.set('X', 10)
    htb.set('L', 50)
    htb.set('C', 100)
    htb.set('D', 500)
    htb.set('M', 1000)

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

    print("count: {}".format(htb.count()))
    print("keys: {}".format(htb.keys()))
    print("values: {}".format(htb.values()))
    print("to_list: {}".format(htb.to_list()))
test()

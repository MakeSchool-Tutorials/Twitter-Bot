from linked_list import *

def test():
    ll = LinkedList()

    a = 'a'
    b = 'b'
    c = 'c'

    ll.append(a)
    ll.append(b)
    ll.append(c)

    print(ll.count() == 3)
    print(ll.all() == [a, b, c])
    print(ll.head.value == a)
    print(ll.tail.value == c)
    print(ll.find(lambda data: data > b) == c)

    print(ll.delete('b') == ll)
    print(ll.all() == [a, c])
    print(ll.delete('f') == None)

    aNode = ll.findNode(lambda node: node.value == a)
    d = 'd'
    ll.insert(d, aNode)

    print(ll.all() == [a, d, c])
test()

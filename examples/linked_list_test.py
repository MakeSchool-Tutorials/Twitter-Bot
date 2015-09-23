from linked_list import *

def test():
    ll = LinkedList()

    a = Node('a')
    b = Node('b')
    c = Node('c')

    ll.append(a)
    ll.append(b)
    ll.append(c)

    print(ll.count() == 3)
    print(ll.all() == [a, b, c])
    print(ll.head == a)
    print(ll.last() == c)
    print(a.next == b)
    print(a.value == 'a')
test()

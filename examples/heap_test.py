from heap import MaxHeap

def test():
    counts = [
        (1, 'one'),
        (3, 'fish'),
        (1, 'two'),
        (2, 'red'),
        (7, 'the'),
        (4, 'ball'),
        (1, 'who')
    ]

    word_heap = MaxHeap(counts)

    print(word_heap.to_list() == [(7, 'the'), (3, 'fish'), (4, 'ball'), (1, 'one'), (2, 'red'), (1, 'two'), (1, 'who')])
    print(word_heap.size == len(counts))
    print(word_heap.root() == (7, 'the'))
    print(word_heap.peek(3) == [(7, 'the'), (3, 'fish'), (4, 'ball')])
    print(word_heap.remove_max() == (7, 'the'))
    print(word_heap.root() == (4, 'ball'))
    word_heap.push((8, 'bank'))
    print(word_heap.root() == (8, 'bank'))
    print(word_heap.take(4) == [(8, 'bank'), (4, 'ball'), (3, 'fish'), (2, 'red')])
test()

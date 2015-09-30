class MaxHeap():
    def __init__(self, source_list=None):
        self.list = [None] # Add null object to make tree arithmetic simpler
        self.size = 0

        if source_list != None:
            self.heapify(source_list)

    def root(self):
        # return root node of heap
        return self.list[1]

    def peek(self, n):
        # look at first n nodes of heap
        return self.list[1:n+1]

    def to_list(self):
        # show heap in list form
        return self.list[1:]

    def push(self, tuple):
        # push item onto heap
        self.list.append(tuple)
        self.size += 1
        self.sift_up(self.size)

    def take(self, n):
        # take n max nodes from heap
        # simple way to get the n max values from heap
        return [self.remove_max() for i in range(n)]

    def remove_max(self):
        # remove the root and restructure heap
        key = self.list[1]
        self.list[1] = self.list.pop()
        self.size -= 1
        self.sift_down(1)
        return key

    def sift_down(self, idx):
        while idx * 2 <= self.size:
            key = self.list[idx]
            max_child_idx = self.max_child(idx)
            max_child = self.list[max_child_idx]
            if max_child > key:
                self.swap(idx, max_child_idx)
            idx = max_child_idx

    def sift_up(self, idx):
        while idx // 2 > 0:
            key = self.list[idx]
            parent_idx = idx // 2
            parent_key = self.list[parent_idx]
            if key > parent_key:
                self.swap(idx, parent_idx)
            idx = parent_idx

    def max_child(self, idx):
        l_idx = idx * 2
        r_idx = idx * 2 + 1

        if r_idx > self.size:
            return l_idx
        if self.list[r_idx] > self.list[l_idx]:
            return r_idx
        else:
            return l_idx

    def swap(self, idx_a, idx_b):
        key = self.list[idx_a]
        self.list[idx_a] = self.list[idx_b]
        self.list[idx_b] = key

    def heapify(self, source_list):
        for item in source_list:
            self.push(item)

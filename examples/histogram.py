def histogram_list(words):
    hstgm = []
    for word in words:
        index = find(word, hstgm)
        if index:
            hstgm[index][1] += 1
        else:
            hstgm.append([word, 1])
    return hstgm

def histogram_tuple(words):
    hstgm = []
    for word in words:
        index = find(word, hstgm)
        if index:
            count = hstgm[index][1]
            hstgm[index] = (word, count + 1)
        else:
            hstgm.append((word, 1))
    return hstgm

def histogram_dict(words):
    hstgm = {}
    for word in words:
        if word in hstgm:
            hstgm[word] += 1
        else:
            hstgm[word] = 1
    return hstgm

def count_list(histogram):
    counts = []
    for word, count in histogram:
        index = find(count, counts)
        if index is not None:
            words = counts[index][1] + [word]
            counts[index] = (count, words)
        else:
            counts.append((count, [word]))
    return counts

def find(item, hstgm):
    for index, pair in enumerate(hstgm):
        if pair[0] == item:
            return index
    return None

if __name__ == '__main__':
    import sys
    hstgm = histogram_list(sys.argv[1:])
    print(count_list(hstgm))
    # print(hstgm)

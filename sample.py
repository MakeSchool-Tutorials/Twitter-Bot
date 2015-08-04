import random
from histogram import histogram_dict

def random_word(histogram):
    return random.choice(histogram.keys())

def probabilistic_random_word(sorted_probabilities):
    limit = sorted_probabilities[-1][0]
    choice = round(random.uniform(0, limit), 4)
    for freq, word in sorted_probabilities:
        if choice < freq:
            return word

def probabilities(freq_dist):
    probabilities = []
    prob = 0
    for word, freq in freq_dist.items():
        prob = round(prob + probability(word, freq_dist), 4)
        probabilities.append((prob, word))
    return sorted(probabilities)

def probability(word, freq_dist):
    numWords = 0
    for _, freq in freq_dist.items():
        numWords += freq
    return round(freq_dist[word] / numWords, 4)

def ensure_randomness(histogram):
    return histogram_dict([random_word(histogram) for i in range(10000)])

def ensure_probability(histogram):
    probs = probabilities(histogram)
    return histogram_dict([probabilistic_random_word(probs) for i in range(10000)])

if __name__ == '__main__':
    import sys
    words = open(sys.argv[1], 'r').read().split()
    hstgm = histogram_dict(words)
    probs = probabilities(hstgm)
    print(probabilistic_random_word(probs))
    print(ensure_probability(hstgm))

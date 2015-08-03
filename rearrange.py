import random

def rearrange(words):
    new_sentence = []
    word_count = len(words)
    for i in range(0, word_count):
        index = random.randint(0, len(words) - 1)
        new_sentence.append(words[index])
        del words[index]

    return new_sentence

if __name__ == '__main__':
    import sys
    new_sentence = rearrange(sys.argv[1:])
    print(' '.join(new_sentence))

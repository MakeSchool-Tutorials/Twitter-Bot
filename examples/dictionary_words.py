import random

def make_sentence(length):
    source = all_words()
    words = list_of_random_words(length, source)
    return ' '.join(words) + '.'

def list_of_random_words(length, words):
    return [random_word(words) for i in range(length)]

def random_word(words):
    return random.choice(words)

def all_words():
    dict_words = '/usr/share/dict/words'
    words_file = open(dict_words, 'r')
    words_str = words_file.read()
    return words_str.split("\n")

if __name__ == '__main__':
    import sys
    sent_length = int(sys.argv[1])
    sent = make_sentence(sent_length)
    print(sent)

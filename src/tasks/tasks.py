import os
import string
import sys
from collections import Counter


def main(argv):
    input_text = 'Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a pellentesque dui, non felis.\n' \
                 'Maecenas malesuada elit lectus felis, malesuada ultricies. Curabitur et ligula. Ut molestie a,' \
                 ' ultricies porta urna.\nVestibulum commodo volutpat a, convallis ac, laoreet enim. Phasellus' \
                 ' fermentum in, dolor. Pellentesque facilisis.'
    letter_occurrence_counter(input_text)
    print()
    celsius_and_fahrenheit(-20, 40, 5)
    print()
    words_counter(argv)
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
    list_range = 2
    some_sum(numbers_list, list_range)
    print()
    pinbal_range()


def letter_occurrence_counter(input_text):
    letters = string.ascii_letters
    counter = Counter(input_text)
    for key in counter:
        if key in letters:
            print('{}: {}'.format(key, counter[key]))


def celsius_and_fahrenheit(min_temp, max_temp, step):
    for c in range(min_temp, max_temp + 1, step):
        print('{} celsius is {} fahrenheit'.format(c, c_to_f(c)))


def c_to_f(c):
    return c * 1.8 + 32


def words_counter(source):
    if source[0] == 'text':
        path = os.path.dirname(os.path.realpath(__file__)) + '/text.txt'
        with open(path, 'r') as from_file:
            lines = from_file.readlines()
            text = ' '.join([line.strip() for line in lines])
            result = count_words(text)
    else:
        result = count_words(source[0])
    with open(os.getcwd() + '/result.txt', 'w') as to_file:
        to_file.writelines(result)


def count_words(text):
    sentences = text.strip('.').split('.')
    result = []
    for i, sentence in enumerate(sentences):
        words = sentence.strip().split(' ')
        result.append('sentence {}: {}\n'.format(i + 1, len(words)))
    return result


def some_sum(numbers_list, list_range):
    result = []
    window_size = list_range * 2 + 1
    list_len = len(numbers_list)
    for i in range(0, list_len):
        min_index = 0 if i - list_range < 0 else i - list_range
        max_index = list_len - window_size + i
        result.append(sum(numbers_list[min_index:max_index]))
    print(result)


def pinbal_range():
    for i in range(1, 101):
        text = ''
        if i % 3 == 0:
            text += 'PIN'
        if i % 7 == 0:
            text += 'BAL'
        print('{}\t{}'.format(i, text))


if __name__ == '__main__':
    main(sys.argv[1:])

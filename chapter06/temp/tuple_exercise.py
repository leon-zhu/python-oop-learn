import datetime
from collections import namedtuple, defaultdict


def middle(stock, date):
    symbol, current, high, low = stock
    return ((high + low) / 2), date


mid_value, date = middle(('FB', 75.0, 75.03, 74), datetime.date(2014, 10, 5))
print(mid_value, date)

Stock = namedtuple('Stock', 'Symbol current high low')
stock = Stock('FB', 75.0, high=75.03, low=74)


def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


def letter_frequency_2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return num_items, []


if __name__ == '__main__':
    # Stock(Symbol='FB', current=75.0, high=75.03, low=74)
    print(stock)

    print(letter_frequency('abcdefafafaf'))

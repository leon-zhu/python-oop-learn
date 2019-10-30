from collections import Counter


def letter_frequency(sentence):
    return Counter(sentence)


if __name__ == '__main__':
    responses = ['aa', 'bfa', 'aa', 'a', 'aa', 'bfa']
    print(Counter(responses).most_common())
    print(Counter(responses).most_common(1))

    print(Counter(responses).most_common(1)[0])
    print(Counter(responses).most_common(1)[0][0])

    print("The children voted for {} ice cream".format(Counter(responses).most_common(1)[0][0]))

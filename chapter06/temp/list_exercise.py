import string


def letter_frequency(sentence):
    # 统计字母和空格
    chars = list(string.ascii_letters) + [" "]
    frequencies = [(c, 0) for c in chars]
    for letter in sentence:
        index = chars.index(letter)
        # print(frequencies[index])
        # print(frequencies[index][1])
        frequencies[index] = (letter, frequencies[index][1] + 1)
    return frequencies


class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)


if __name__ == '__main__':
    print(letter_frequency('abddaedfs'))

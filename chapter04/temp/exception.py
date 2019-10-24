class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


def funny_division(number):
    try:
        if number == 13:
            raise ValueError("13 is an unlucky number")
        print(100 / number)
    except Exception as e:
        print("Enter a number other than zero: ", e)


class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.balance = balance
        self.amount = amount

    def overage(self):
        return self.amount - self.balance


def test_invalid_param():
    try:
        raise InvalidWithdrawal(25, 20)
    except InvalidWithdrawal as e:
        print("I'm sorry, but money is ${}".format(e.overage()))


if __name__ == '__main__':
    test_invalid_param()

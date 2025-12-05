# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __lt__(self, another):
        return (
            self.__euros < another.__euros
            or self.__euros == another.__euros
            and self.__cents < another.__cents
        )

    def __gt__(self, another):
        return (
            self.__euros > another.__euros
            or self.__euros == another.__euros
            and self.__cents > another.__cents
        )

    def __ne__(self, another):
        return not self.__eq__(another)

    def __add__(self, another):
        result = Money(self.__euros, self.__cents)
        result.__cents = (result.__cents + another.__cents) % 100
        result.__euros = (
            result.__euros + another.__euros + (self.__cents + another.__cents) // 100
        )
        return result

    def __sub__(self, another):
        if self.__lt__(another):
            raise ValueError("a negative result is not allowed")
        result = Money(self.__euros, self.__cents)
        if result.__cents < another.__cents:
            result.__cents = 100 + result.__cents - another.__cents
            result.__euros = result.__euros - another.__euros - 1
        else:
            result.__cents -= another.__cents
            result.__euros -= another.__euros
        return result


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

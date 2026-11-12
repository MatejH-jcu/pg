class mojevyjimka(Exception):
    pass


class Bankovniucet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.__zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self.__zustatek}"

    def vloz(self, castka):
        if castka <= 0:
            raise mojevyjimka("Částka musí být větší než nula.")
        self.__zustatek += castka

    def vyber(self, castka):
        if castka <= 0:
            raise mojevyjimka("Částka musí být větší než nula.")
        if castka > self.__zustatek:
            raise mojevyjimka("Na účtu není dostatek peněz.")
        self.__zustatek -= castka

    def pricti_uroky(self):
        self.__zustatek += self.__zustatek * self.urok


if __name__ == "__main__":
    ucet = Bankovniucet("sporici", 0.05)
    ucet.vloz(1)
    ucet.vyber(1)
    ucet.pricti_uroky()
    print(ucet)

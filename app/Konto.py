import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, promotion_code=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = promotion_code
        self.pesel = pesel

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, pesel):
        if (len(pesel) != 11):
            self._pesel = "Niepoprawny pesel!"
        else:
            self._pesel = pesel

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, promotion_code):
        if (promotion_code and re.match(r"PROM_[^\s][^\s][^\s]$", promotion_code)):
            self._saldo = 50
        else:
            self._saldo = 0



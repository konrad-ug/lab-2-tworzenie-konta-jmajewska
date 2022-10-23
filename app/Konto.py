import re


def is_promotion_code_correct(promotion_code):
    if(re.match(r"PROM_[^\s][^\s][^\s]$", promotion_code)):
        return True
    return False

def is_year_of_birdth_goof_for_promotion(pesel):
    year = int(pesel[:2])
    century = int(pesel[2:4])

    if (year < 60 and century > 20):
        return True
    elif(year > 60):
        return True
    return False


class Konto:
    def __init__(self, imie, nazwisko, pesel, promotion_code=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = (promotion_code, pesel)
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
    def saldo(self, args):
        promotion_code, pesel = args
        if (promotion_code and is_promotion_code_correct(promotion_code) and is_year_of_birdth_goof_for_promotion(pesel)):
            self._saldo = 50
        else:
            self._saldo = 0


# konto = Konto("J", "M", "61000000000", "PROM_XYZ")
# print(konto.saldo)
print(is_promotion_code_correct("PROM_XYZ"))
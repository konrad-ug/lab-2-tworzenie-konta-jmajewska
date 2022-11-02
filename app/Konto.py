import re


def is_promotion_code_correct(promotion_code):
    if (re.match(r"PROM_[^\s][^\s][^\s]$", promotion_code)):
        return True
    return False


def is_year_of_birdth_goof_for_promotion(pesel):
    year = int(pesel[:2])
    century = int(pesel[2:4])

    if (year < 60 and century > 20):
        return True
    elif (year > 60):
        return True
    return False


class KontoBase:
    def __init__(self):
        pass
    
    isPrivate = False
    isFirm = False


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

    def send(self, amount):
        saldo_after_transfer = self.saldo - amount
        if (saldo_after_transfer < 0):
            return False
        else:
            self._saldo = saldo_after_transfer
            return True

    def recieve(self, amount):
        self._saldo = self.saldo + amount

    def send_fast(self, amount):
        if(isinstance(self, KontoFirmowe)):
            charge = 5
        else:
            charge = 1

        saldo_after_transfer = self.saldo - amount - charge

        if(saldo_after_transfer < -charge):
            return False
        else: 
            self._saldo = saldo_after_transfer


class KontoFirmowe(Konto):
    def __init__(self,firm_name,nip,imie="",nazwisko="",pesel=""):
        super().__init__(self,imie,nazwisko,pesel)
        self.firm_name = firm_name
        self.nip = (nip)

    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self,nip):
        if(len(nip) != 10):
            self._nip = "Niepoprawny nip"
        else: 
            self._nip = nip
    

konto = KontoFirmowe("k","p")
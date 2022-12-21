import re
import requests

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


class Konto:
    charge = 1
    def __init__(self, imie, nazwisko, pesel, promotion_code=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = (promotion_code, pesel)
        self.pesel = pesel
        self.history = []


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
            self._create_history(amount)
            return True

    def recieve(self, amount):
        self._saldo = self.saldo + amount
        self._create_history(amount)

        
    def send_fast(self, amount):
        saldo_after_transfer = self.saldo - amount - self.charge

        if(saldo_after_transfer < -self.charge):
            return False
        else: 
            self._saldo = saldo_after_transfer
            self._create_history(amount)

    def _create_history(self,amount):
         self.history.append(amount)

    def get_credit(self,amount):
        three_last_operations = self.history[-3:]
        three_last_operations_result = len(list(filter(lambda a : a > 0, three_last_operations))) == 3
        if(len(self.history) >= 5):
            five_last_operations = self.history[-5:]
        else:
            five_last_operations = []
        five_last_operations_sum = 0

        for i in five_last_operations:
            five_last_operations_sum += abs(int(i))
        
        five_last_operations_result = five_last_operations_sum > amount

        if  three_last_operations_result or five_last_operations_result:
            self._saldo += amount
            return True
        else:
            return False
        



class KontoFirmowe(Konto):
    charge = 5
    def __init__(self,firm_name,nip,imie="",nazwisko="",pesel=""):
        super().__init__(self,imie,nazwisko,pesel)
        self.firm_name = firm_name
        if(not self.check_if_NIP_is_valid(nip)):
            self._nip = "Pranie"
        else:
            self.nip = (nip)

    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self,nip):
            self._nip = nip
    
    def get_credit(self, amount):
        zus_transfer = -1775
        if(self.saldo >= 2*amount and (zus_transfer in self.history)):
            self._saldo += amount
            return True
        else:
            return False

    @classmethod
    def check_if_NIP_is_valid(cls,nip):
        print("test")
        BANK_APP_MF_URL = "https://wl-api.mf.gov.pl"
        r = requests.get(f"{BANK_APP_MF_URL}//api/search/nip/{nip}?date=2022-12-08")
        if(r.status_code == 200):
            return True
        else:
            return False

class RejestrKont:
    rejestr = []

    @classmethod
    def addKonto(cls,konto):
        cls.rejestr.append(konto)
    
    @classmethod
    def findKonto(cls,pesel):
        for konto in cls.rejestr:
            if(konto.pesel == pesel):
                return konto
        return "There is no such an account"
        

    @classmethod
    def kontoCount(cls):
        return len(cls.rejestr)
    
    @classmethod
    def kontoUpdate(cls,pesel=None,imie=None,nazwisko=None,saldo=None):
        konto = cls.findKonto(pesel)
        if(konto != "There is no such an account"):
            if(imie):
                konto.imie = imie
            if(nazwisko):
                konto.nazwisko = nazwisko
            if(saldo):
                konto._saldo = saldo
            return konto
        else:
            return None
    
    @classmethod
    def kontoDelete(cls,pesel):
        konto = cls.findKonto(pesel)
        if(konto == "There is no such an account"):
            return None
        else: 
            new_rejestr = []
            # filtered_rejestr = filter(lambda konto : konto.pesel == pesel, cls.rejestr)
            for konto in cls.rejestr:
                if(konto.pesel != pesel):
                    new_rejestr.append(konto)
            cls.rejestr = new_rejestr
class RejestrKont:
    rejestr = []

    @classmethod
    def addKonto(cls,konto):
        cls.rejestr.append(konto)
        # print(cls.rejestr)
    
    @classmethod
    def findKonto(cls,pesel):
        for konto in cls.rejestr:
            if(konto.pesel == pesel):
                return konto
        return "There is no such an account"
        

    @classmethod
    def kontoCount(cls):
        return len(cls.rejestr)
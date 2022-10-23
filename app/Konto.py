class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
    
    @property
    def pesel(self):
        return self._pesel
    
    @pesel.setter
    def pesel(self, pesel): 
        if(len(pesel) != 11):
            self._pesel = "Niepoprawny pesel!"
        else: 
            self._pesel = pesel
    


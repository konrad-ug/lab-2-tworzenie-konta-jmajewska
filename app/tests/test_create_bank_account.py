import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "00000000000")
        self.assertEqual(pierwsze_konto.imie, "Dariusz",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski",
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "00000000000",
                         "Pesel nie został wpisany")
    # tutaj proszę dodawać nowe testy

    def test_pesel_validity(self):
        konto_1 = Konto("Name", "Surname", '000000')
        self.assertNotEqual(len(konto_1.pesel), 11)
        self.assertEqual(konto_1.pesel, "Niepoprawny pesel!")

        konto_2 = Konto("Name", "Surname", "00000000000")
        self.assertEqual(len(konto_2.pesel), 11)
        self.assertEqual(konto_2.pesel, "00000000000")

from cmath import exp
import unittest

from ..Konto import Konto,KontoFirmowe, is_year_of_birdth_goof_for_promotion, is_promotion_code_correct


class TestUtilFunctionsForCreatingBankAccount(unittest.TestCase):
  
    def test_year_of_birth(self):
        peselafter60century20 = "90000000000"
        peselbefore60century20 = "40000000000"
        peselafter60century21 = "02210000000"

        actual = is_year_of_birdth_goof_for_promotion(peselafter60century20)
        expected = True
        self.assertEqual(actual, expected)

        actual = is_year_of_birdth_goof_for_promotion(peselbefore60century20)
        expected = False
        self.assertEqual(actual,expected)

        actual = is_year_of_birdth_goof_for_promotion(peselafter60century21)
        expected = True
        self.assertEqual(actual,expected)

    def test_promotion_code(self):
        mocked_promotion_code_correct = "PROM_XYZ"
        mocked_promotion_code_wrong_prefix = "COS_XYZ"
        mocked_promotion_code_wrong_suffix = "PROM_XYZZ"

        actual = is_promotion_code_correct(mocked_promotion_code_correct)
        expected = True
        self.assertEqual(actual,expected)

        actual = is_promotion_code_correct(mocked_promotion_code_wrong_prefix)
        expected = False
        self.assertEqual(actual, expected)

        actual = is_promotion_code_correct(mocked_promotion_code_wrong_suffix)
        expected = False
        self.assertEqual(actual, expected)

class TestCreateBankAccount(unittest.TestCase):

    mocked_name = "Dariusz"
    mocked_surname = "Janiszewski"
    mocked_pesel_wrong_length = "0000000"
    mocked_correct_pesel = "00000000000"
    mocked_pesel_too_old_for_promotion = "500000000"
    mocked_pesel_correct_for_promotion = "61000000000"

    mocked_saldo_no_promotion_code = 0
    mocked_saldo_with_promotion_code = 50

    mocked_incorrect_pesel_message = "Niepoprawny pesel!"
    mocked_promotion_code_correct = "PROM_XYZ"
    mocked_promotion_code_wrong = "PROM_XYZZaxs"
    

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_correct_pesel)
        self.assertEqual(pierwsze_konto.imie, self.mocked_name,
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.mocked_surname,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.mocked_correct_pesel,
                         "Pesel nie został podany")
    # tutaj proszę dodawać nowe testy

    def test_pesel_validity(self):
        konto_1 = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel_wrong_length)
        self.assertNotEqual(len(konto_1.pesel), 11)
        self.assertEqual(konto_1.pesel, self.mocked_incorrect_pesel_message)

        konto_2 = Konto(self.mocked_name, self.mocked_surname, self.mocked_correct_pesel)
        self.assertEqual(len(konto_2.pesel), 11)
        self.assertEqual(konto_2.pesel, self.mocked_correct_pesel)

    def test_promotion_code(self): 
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_correct_pesel)
        self.assertEqual(konto.saldo, 0)

        konto = Konto(self.mocked_name, self.mocked_surname,self.mocked_pesel_correct_for_promotion, self.mocked_promotion_code_correct)
        self.assertEqual(konto.saldo, 50)

        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_correct_pesel, self.mocked_promotion_code_wrong)
        self.assertEqual(konto.saldo, 0)

        

    def test_promotion_code_accessibility(self):
        konto = Konto(self.mocked_name,self.mocked_surname, self.mocked_pesel_correct_for_promotion, self.mocked_promotion_code_correct)
        self.assertEqual(konto.saldo, 50)

        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_correct_pesel, self.mocked_promotion_code_wrong)
        self.assertEqual(konto.saldo, 0)

    def test_create_konto_firmowe(self):
        konto = KontoFirmowe("name", "xxxxxxxxxx")
        self.assertEqual(konto.nip, "Pranie")
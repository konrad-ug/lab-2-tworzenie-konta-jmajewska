from ..Konto import Konto, KontoFirmowe
import unittest


class TestCredit(unittest.TestCase):
    konto_fail = Konto("imie", "nazwisko", "00000000000")
    konto_fail._saldo = 1000
    konto_fail.history = [-100, 200, -200, 300, 100]
    credit_fail = 2000
    credit_success = 900
    konto_success = Konto("imie", "nazwisko", "00000000000")
    konto_success._saldo = 1000
    konto_success.history = [-100, 200, -200, 300, 100]

    def test_credit_fail(self):
        self.konto_fail.get_credit(300)
        self.assertEqual(self.konto_fail.saldo, 1000)
    
    def test_credit_success(self):
        self.konto_success.get_credit(self.credit_success)
        self.assertEqual(self.konto_success.saldo, 1900)
        
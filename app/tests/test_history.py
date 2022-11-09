from ..Konto import Konto,KontoFirmowe
import unittest

class TestAccountHistory(unittest.TestCase):
    def test_empty_history(self):
        konto = Konto("imie","nazwisko","00000000000")
        self.assertEqual(len(konto.history),0)

    def test_history_not_empty_once(self):
        konto = Konto("imie","nazwisko","00000000000")
        konto._saldo = 5000
        konto.send(10)
        self.assertEqual(len(konto.history), 1)
    
    def test_history_not_empty_n(self):
        konto = Konto("imie","nazwisko","00000000000")
        konto._saldo = 5000
        konto.recieve(100)
        konto.recieve(100)
        self.assertEqual(len(konto.history), 2)

    def test_history_not_empty_n_company(self):
        konto = KontoFirmowe("firma","00000000000")
        konto._saldo = 5000
        konto.recieve(100)
        konto.send(100)
        self.assertEqual(len(konto.history), 2)

    def test_history_empty_company(self):
        konto = KontoFirmowe("firma","00000000000")
        konto._saldo = 5000
        self.assertEqual(len(konto.history), 0)


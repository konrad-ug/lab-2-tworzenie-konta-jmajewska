import unittest
from ..Konto import Konto

class TestTransfers(unittest.TestCase):
    mocked_name = "Name"
    mocked_surname = "Surname"
    mocked_amount = 800
    mocked_saldo_too_little = 100
    mocked_saldo_enough = 1000
    mocked_pesel = "61200000000"

    def test_send_transfer_correct(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_enough
        konto.send(self.mocked_amount)
        self.assertEqual(konto.saldo, self.mocked_saldo_enough - self.mocked_amount)

    def test_send_transfer_saldo_too_little(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_too_little
        konto.send(self.mocked_amount)
        self.assertEqual(konto.saldo, self.mocked_saldo_too_little)
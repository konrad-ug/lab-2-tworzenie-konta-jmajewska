import unittest
from ..Konto import Konto, KontoFirmowe


class TestTransfers(unittest.TestCase):
    mocked_name = "Name"
    mocked_surname = "Surname"
    mocked_amount = 800
    mocked_amount_edge = 1000
    mocked_saldo_too_little = 100
    mocked_saldo_enough = 1000
    mocked_pesel = "61200000000"
    mocked_nip = "0000000000"
    mocked_nip_wrong = "000"

    def test_send_transfer_correct(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_enough
        konto.send(self.mocked_amount)
        self.assertEqual(
            konto.saldo, self.mocked_saldo_enough - self.mocked_amount)

    def test_send_transfer_saldo_too_little(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_too_little
        konto.send(self.mocked_amount)
        self.assertEqual(konto.saldo, self.mocked_saldo_too_little)

    def test_send_transfer_on_edge(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_enough
        konto.send(self.mocked_amount_edge)
        self.assertEqual(
            konto.saldo, self.mocked_saldo_enough - self.mocked_amount_edge)

    def test_receive_transfer(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = 0
        konto.recieve(self.mocked_amount)
        self.assertEqual(konto.saldo, self.mocked_amount)

    def test_firm_account_create_wrong_nip(self):
        konto_firmowe = KontoFirmowe(self.mocked_name,self.mocked_nip_wrong)
        self.assertEqual(konto_firmowe.nip, "Niepoprawny nip")
    
    def test_firm_account_correct_nip(self):
        konto_firmowe = KontoFirmowe(self.mocked_name,self.mocked_nip)
        self.assertEqual(len(konto_firmowe.nip), 10)

    def test_fast_transfer_enough_money(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_enough
        konto.send_fast(self.mocked_amount)
        self.assertEqual(konto.saldo, self.mocked_saldo_enough - self.mocked_amount - 1)
    
    def test_fast_transfer_not_enough_money(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_saldo_too_little
        self.assertEqual(konto.saldo, self.mocked_saldo_too_little)

    def test_fast_transfer_on_edge(self):
        konto = Konto(self.mocked_name, self.mocked_surname, self.mocked_pesel)
        konto._saldo = self.mocked_amount_edge
        konto.send_fast(self.mocked_amount_edge)
        self.assertEqual(konto.saldo, self.mocked_amount_edge - self.mocked_amount_edge - 1)
    
    def test_fast_transfer_correct_company_account(self):
        konto_firmowe = KontoFirmowe(self.mocked_name, self.mocked_nip)
        konto_firmowe._saldo = self.mocked_saldo_enough
        konto_firmowe.send_fast(self.mocked_amount)
        self.assertEqual(konto_firmowe.saldo, self.mocked_saldo_enough - self.mocked_amount - 5)

    def test_fast_transfer_on_edge_company_account(self):
        konto_firmowe = KontoFirmowe(self.mocked_name,self.mocked_nip)
        konto_firmowe._saldo = self.mocked_amount
        konto_firmowe.send_fast(self.mocked_amount)
        self.assertEqual(konto_firmowe.saldo, -5)

    def test_fast_transfer_not_enough_money_company_account(self):
        konto_firmowe = KontoFirmowe(self.mocked_name,self.mocked_nip)
        konto_firmowe._saldo = self.mocked_amount
        konto_firmowe.send_fast(self.mocked_amount_edge)
        self.assertEqual(konto_firmowe.saldo, self.mocked_amount)
from ..Konto import Konto
import unittest
from ..RejestrKont import RejestrKont


class TestRejest(unittest.TestCase):
    def setUp(self):
        konto = Konto('i', 'n', '00000000007')
        rejestr = RejestrKont()
        rejestr.addKonto(konto)

    def tearDown(self):
        RejestrKont.rejestr = []

    def test_rejestr_konto_empty_list(self):
        count = RejestrKont.kontoCount()
        self.assertEqual(count, 1)

    def test_konto_find_existing_konto(self):
        konto = Konto('i', 'n', '00000000009')
        RejestrKont.addKonto(konto)
        konto_found = RejestrKont.findKonto("00000000009")
        self.assertEqual(konto_found, konto)

    def test_konto_find_not_existing_konto(self):
        konto = Konto('i', 'n', '00000000006')
        result = RejestrKont.findKonto(konto)
        proper_result = "There is no such an account"
        self.assertEqual(result, proper_result)

    def test_rejestr(self):
        konto = Konto('i', 'n', '00000000000')
        konto1 = Konto('i', 'n', '00000000001')
        konto2 = Konto('i', 'n', '00000000002')
        RejestrKont.addKonto(konto)
        RejestrKont.addKonto(konto1)
        RejestrKont.addKonto(konto2)
        self.assertEqual(len(RejestrKont.rejestr), 4)

    def test_rejestr_count(self):
        konto = Konto('i', 'n', '00000000000')
        konto1 = Konto('i', 'n', '00000000001')
        konto2 = Konto('i', 'n', '00000000002')
        RejestrKont.addKonto(konto)
        RejestrKont.addKonto(konto1)
        RejestrKont.addKonto(konto2)
        self.assertEqual(RejestrKont.kontoCount(), 4)

    def test_delete_existing_konto(self):
        konto = Konto('i', 'n', '00000000007')
        konto2 = Konto('i', 'n', '00000000008')
        RejestrKont.addKonto(konto2)
        rejest_len = len(RejestrKont.rejestr)
        RejestrKont.kontoDelete(konto.pesel)
        rejestr_len_after_deletion = len(RejestrKont.rejestr)
        self.assertEqual(rejestr_len_after_deletion, rejest_len-1)

    def test_delete_not_existing_konto(self):
        konto = Konto('i', 'n', '00000000000')
        rejestr_len = len(RejestrKont.rejestr)
        result = RejestrKont.kontoDelete(konto.pesel)
        rejestr_len_after_deletion = len(RejestrKont.rejestr)
        self.assertEqual(rejestr_len,rejestr_len_after_deletion)
        self.assertEqual(result,None)

    def test_update_not_existing_konto(self):
        konto = Konto('i', 'n', '00000000000')
        result = RejestrKont.kontoUpdate(konto.pesel,"Julia")
        self.assertEqual(result,None)

    def test_update_existing_konto(self):
        konto = Konto('i', 'n', '00000000007')
        result = RejestrKont.kontoUpdate(konto.pesel,"Julia","Majewska",50)
        self.assertEqual(result.imie, "Julia")
        self.assertEqual(result.nazwisko, "Majewska")
        self.assertEqual(result.saldo, 50)

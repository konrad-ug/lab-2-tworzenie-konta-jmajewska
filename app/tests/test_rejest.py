from ..Konto import Konto
import unittest
from ..RejestrKont import RejestrKont

class TestRejest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        konto = Konto('i','n','00000000000')
        rejestr = RejestrKont()
        rejestr.addKonto(konto)
    @classmethod
    def tearDownClass(cls):
        RejestrKont.rejestr = []

    def rejestr_konto_empty_list(self):
        count = RejestrKont.kontoCount()
        self.assertEqual(count,1)        

    def test_konto_find_existing_konto(self):
        konto = Konto('i','n','00000000009')
        RejestrKont.addKonto(konto)
        konto_found = RejestrKont.findKonto("00000000009")
        self.assertEqual(konto_found,konto)

    def konto_find_not_existing_konto(self):
        konto = Konto('i','n','0000000000x')
        self.assertEqual(RejestrKont.findKonto(konto),"There is no such an account")


    def test_rejestr(self):
        konto = Konto('i','n','00000000000')
        konto1 = Konto('i','n','00000000001')
        konto2 = Konto('i','n','00000000002')
        RejestrKont.addKonto(konto)
        RejestrKont.addKonto(konto1)
        RejestrKont.addKonto(konto2)
        self.assertEqual(len(RejestrKont.rejestr), 5)

    def test_rejestr_count(self):
        rejestr = RejestrKont()
        self.assertEqual(rejestr.kontoCount(),5)
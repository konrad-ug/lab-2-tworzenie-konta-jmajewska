from ..Konto import Konto,KontoFirmowe
import unittest
from unittest.mock import patch,Mock

class TestAccountHistory(unittest.TestCase):

    def _mock_response(self, status):
        return Mock(status_code=status)
    
    
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

    @patch('requests.get')
    def test_history_not_empty_n_company(self,mock_get):
        mock_response = self._mock_response(200)
        mock_get.return_value = mock_response
        konto = KontoFirmowe("firma","00000000000")
        konto._saldo = 5000
        konto.recieve(100)
        konto.send(100)
        self.assertEqual(len(konto.history), 2)

    def test_history_empty_company(self):
        konto = KontoFirmowe("firma","00000000000")
        konto._saldo = 5000
        self.assertEqual(len(konto.history), 0)


from ..Konto import Konto, KontoFirmowe
import unittest
from unittest.mock import patch,Mock
from parameterized import parameterized


class TestCredit(unittest.TestCase):

    
    def _mock_response(self, status):
        return Mock(status_code=status)
    
    def setUp(self):
        self.konto = Konto("imie", "nazwisko", "00000000000")
        self.konto._saldo = 1000

    @parameterized.expand(
        [
            ([1, 1, 1, 1, 900], 300, True),
            ([-1, -1, -1, -1, -300], 203, True)
        ]
    )
    def test_credit_success(self, history, credit, given):
        self.konto.history = history
        is_given = self.konto.get_credit(credit)
        self.assertEqual(is_given, given)

    @parameterized.expand(
        [
            ([-100, -200, 300, 100], 300, False),
            ([100, 233], 100, False),
            ([1, 1, 1, 1, -100], 200, False),
            ([], 100, False),
        ]
    )
    def test_credit_fail(self, history, credit, given):
        self.konto.history = history
        czy_przyznany = self.konto.get_credit(credit)
        self.assertEqual(self.konto.saldo, 1000)
        self.assertEqual(czy_przyznany, given)

class TestCompanyCredit(unittest.TestCase):

    @patch('request.get')
    def setUp(self,mock_get):
        mock_response = self._mock_response(200)
        mock_get.return_value = mock_response
        self.konto = KontoFirmowe('firma','1111111111')
        self.konto._saldo = 2000

    @parameterized.expand(
        [
            ([100,100,-200],1000 ,False),
            ([100,-1775,200],3000,False)
        ]
    )
    def test_company_history_fail(self,history,credit,given):
        self.konto.history = history
        is_given = self.konto.get_credit(credit)
        self.assertEqual(is_given,given)

    @parameterized.expand(
        [
            ([100,-1775],500,True),
            ([100,1775,-1775],1000,True)
        ]
    )
    def test_company_credit_succeed(self,history,credit,given):
        self.konto.history = history
        is_given = self.konto.get_credit(credit)
        self.assertEqual(is_given,True)
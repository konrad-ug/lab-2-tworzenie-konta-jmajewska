from ..Konto import Konto, KontoFirmowe
import unittest
from parameterized import parameterized


class TestCredit(unittest.TestCase):
    # konto_fail._saldo = 1000
    # konto_fail.history = [-100, 200, -200, 300, 100]
    # credit_fail = 2000
    # credit_success = 900
    # konto_success._saldo = 1000
    # konto_success.history = [-100, 200, -200, 300, 100]
    # konto_fail_too_short._saldo = 1000
    # konto_fail_too_short.history = [200, -200, 300, 100]

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


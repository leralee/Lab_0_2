import unittest
import pytest
from unittest import mock

from currency import get_total_currency_value, get_currency_value_from_api


class TestCurrency(unittest.TestCase):

    @pytest.mark.base
    def test_currency_positive(self):
        res = get_total_currency_value(
            rate='GBP',
            count=100_000,
            discount=100
       )
        self.assertEqual(res, 1068.07)

    @pytest.mark.base
    def test_currency_negative(self):
        with self.assertRaises(ValueError) as err:
            get_total_currency_value('GBP', 100_000, -1)

    @pytest.mark.api
    def test_currency_with_api(self):
        with mock.patch('currency.get_currency_value_from_api') as mock_currency:
            mock_currency.return_value = 0.0131962
            res = get_total_currency_value(
                rate = 'GBP',
                count = 100_000,
                discount=100
            )
            self.assertEqual(res, 1219.62)



# ------ TESTS RESULTS ------


# test_currency.py::TestCurrency::test_currency_negative PASSED
# test_currency.py::TestCurrency::test_currency_positive PASSED
# test_currency.py::TestCurrency::test_currency_with_api PASSED



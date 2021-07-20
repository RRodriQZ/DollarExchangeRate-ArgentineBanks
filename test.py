from functions.functions import get_partial_values_from_banks
from scrap.argentine_banks_scrap import ArgentineBanksScrap
import unittest


class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.argentine_banks_values = ArgentineBanksScrap().get_dollar_values_of_banks()
        self.icbc_url = 'https://www.infodolar.com/cotizacion-dolar-entidad-icbc.aspx'
        self.argentine_banks_list = []

    def tearDown(self):
        pass

    def test_argentine_banks_list_is_zero(self):
        length_argentine_banks = len(self.argentine_banks_list)
        self.assertEqual(length_argentine_banks, 0)

    def test_banco_nacion_values(self):
        bank_found = list(filter(lambda bank: bank.get_bank_name() == 'Banco Nacion', self.argentine_banks_values))
        bank_name = bank_found[0].get_bank_name()
        self.assertEqual(bank_name, 'Banco Nacion')

    def test_banco_galicia_values(self):
        bank_found = list(filter(lambda bank: bank.get_bank_name() == 'Banco Galicia', self.argentine_banks_values))
        bank_name = bank_found[0].get_bank_name()
        self.assertEqual(bank_name, 'Banco Galicia')

    def test_banco_ICBC_values_types(self):
        partial_values = get_partial_values_from_banks(self.icbc_url)
        value_type_1 = type(partial_values[0])
        value_type_2 = type(partial_values[1])
        value_type_3 = type(partial_values[2])
        value_type_4 = type(partial_values[3])

        self.assertEqual(value_type_1, float)
        self.assertEqual(value_type_2, float)
        self.assertEqual(value_type_3, float)
        self.assertEqual(value_type_4, float)

    def test_argentine_banks_list_is_eleven(self):
        self.argentine_banks_list.extend(self.argentine_banks_values)
        length_argentine_banks = len(self.argentine_banks_list)
        self.assertEqual(length_argentine_banks, 11)


if __name__ == '__main__':
    unittest.main()

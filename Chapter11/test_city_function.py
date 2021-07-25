import unittest
from city_functions import get_city_country

class NameTestCase(unittest.TestCase):
    """TESTS FOR GET_CITY_COUNTRY"""

    def test_get_city_country(self):
        """DOES 'SANTIAGO, CHILE' WORK?"""
        formatted = get_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_get_city_country_population(self):
        formatted = get_city_country('santiago', 'chile', 5_000_000)
        self.assertEqual(formatted, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
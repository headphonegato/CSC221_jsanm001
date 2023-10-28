import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        nyc_usa = city_country('nyc', 'usa')
        self.assertEqual(nyc_usa, 'NYC, USA')

if __name__ == '__main__':
    unittest.main()

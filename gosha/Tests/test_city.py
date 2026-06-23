import unittest
from city_functions import city_functions

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		describe_city = city_functions('kamyshin', 'russia')
		self.assertEqual(describe_city, "Kamyshin, Russia")

if __name__ == '__main__':
	unittest.main()
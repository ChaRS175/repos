import unittest
from formatted_name import get_formatted_name

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('pines', 'pineapplesovich')
		self.assertEqual(formatted_name, "Pines Pineapplesovich")

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('pines', 'pineapplesovich', 'pineapple')
		self.assertEqual(formatted_name, "Pines Pineapple Pineapplesovich")

if __name__ == '__main__':
	unittest.main()

# упражнения




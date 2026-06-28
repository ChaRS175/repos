import unittest
from employee import Employee

class TestClassEmployee(unittest.TestCase):

	def setUp(self):
		self.employee = Employee('Pines', 'Pineapple', 40000)
		self.employee_data = ['Pines', 'Pineapple', 40000]

	def test_give_default_raise(self):
		self.employee.give_raise(5000)
		self.assertEqual(self.employee.money, 45000)

	def test_give_custom_raise(self):
		self.employee.give_raise(10000)
		self.assertEqual(self.employee.money, 50000)

if __name__ == '__main__':
	unittest.main()



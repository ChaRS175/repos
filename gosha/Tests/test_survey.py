import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_response = AnonymousSurvey(question)
		self.responses = ['English', 'Deutch', 'Ispanol']

	def test_store_single_response(self):
		self.my_response.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_response.responses)

	def test_store_three_responses(self):
		for response in self.responses:
			self.my_response.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_response.responses)

if __name__ == '__main__':
	unittest.main()

# упражнения

# 1.
# 2.
# 3.

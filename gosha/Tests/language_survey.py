from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_response = AnonymousSurvey(question)

my_response.show_question()
print("Enter 'q' to quit\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_response.store_response(response)

print("\nThank you to everyone who participated in the survey")
my_response.show_results()
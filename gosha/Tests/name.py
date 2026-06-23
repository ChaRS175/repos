from formatted_name import get_formatted_name

print("Enter 'q' to quit")
while True:
	first = input("\nEnter your firstname: ")
	if first == 'q':
		break
	last = input("Enter your lastname: ")
	if last == 'q':
		break

	formatted_name =  get_formatted_name(first, last)
	print(f"\n\tFormatted name: {formatted_name}")
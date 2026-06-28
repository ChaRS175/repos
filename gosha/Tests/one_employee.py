from employee import Employee

print("Enter 'q' to quit\n")
while True:
	employee_name = input("Name: ")
	if employee_name.lower() == 'q':
		break

	employee_lastname = input("Lastname: ")
	if employee_lastname == 'q':
		break

	employee_raise = input("Year raise: ")
	if employee_raise == 'q':
		break

	employee = Employee(employee_name, employee_lastname, 40000)

	if employee_raise:
		employee.give_raise(employee_raise)
	else:
		employee.give_raise(5000) 

print("We save your data in archive")

employee.show_data()
	
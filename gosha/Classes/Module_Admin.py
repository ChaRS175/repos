import Module_User as MU

class Privileges():
	def __init__(self, *privileges):
		self.privileges = privileges

	def show_privileges(self):
		print(f"Your privileges:")
		for privilege in self.privileges:
			print(f"\tYou can {privilege}")


class Admin(MU.User):
	def __init__(self, first_name, last_name, *privileges):
		super().__init__(first_name, last_name, privileges)
		self.privileges = Privileges(*privileges)


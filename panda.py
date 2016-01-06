class Panda:
	def __init__(self, name, email, gender):
		self.name = name
		self.email = email
		self.gender = gender

	def __str__(self):
		return '{}, {}, {}'.format(self.name, self.email, self.gender)

    #def __repr__(self):
     #   return "Panda('{}', '{}', '{}')".format(self.name, self.email, self.gender)

	def __eq__(self, other):
		return self.name == other.name and self.email == other.email and self.gender == other.gender

	def __hash__(self):
		return hash(self.name + 'pandapanda')

	def name(self):
		return self.name

	def email(self):
		if self.email.split('@')[1] == 'pandamail.com':
			return self.email
		return False

	def gender(self):
		return self.gender

	def isMale(self):
		return self.gender == "male"

	def isFemale(self):
		return self.gender == "female"

class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def __str__(self):
        return '{}, {}, {}'.format(self.__name, self.__email, self.__gender)

        #def __repr__(self):
        #   return "Panda('{}', '{}', '{}')".format(self.name, self.email, self.gender)

    def __eq__(self, other):
        return self.__name == other.__name and self.__email == other.__email and self.__gender == other.__gender

    def __hash__(self):
        return hash(self.__name + 'pandapanda')

    def name(self):
        return self.__name

    def email(self):
        if self.__email.split('@')[1] == 'pandamail.com':
            return self.__email
        return False

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def panda_to_dict(self):
        return str(self.__dict__)

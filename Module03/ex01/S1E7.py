from S1E9 import Character

class Baratheon(Character):
	"""Representing the Baratheon family."""
	def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='brown', hairs='dark'):
		super().__init__(first_name, is_alive)
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs

	def die(self):
		self.is_alive = False

	def __str__(self):
		vector = self.family_name, self.eyes,self.hairs
		return f"Vector: {vector}"
	
	def __repr__(self):
		vector = self.family_name, self.eyes,self.hairs
		return f"Vector: {vector}"

class Lannister(Character):
	"""Representing the Lannister family."""

	def __init__(self, first_name, is_alive=True, family_name='Lannister', eyes='blue', hairs='light'):
		super().__init__(first_name, is_alive)
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs

	def die(self):
		self.is_alive = False

	def __str__(self):
		vector = self.family_name, self.eyes,self.hairs
		return f"Vector: {vector}"

	def __repr__(self):
		vector = self.family_name, self.eyes,self.hairs
		return f"Vector: {vector}"

	def decorator(func):
		def inner1(first_name, is_alive):
			return func(first_name, is_alive)
		return inner1

	@decorator
	def create_lannister(first_name, is_alive=True):
		return Lannister(first_name, is_alive)
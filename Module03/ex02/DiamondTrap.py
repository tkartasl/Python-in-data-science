from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	def __init__(self, first_name):
		Baratheon.__init__(self, first_name)
		Lannister.__init__(self, first_name)

	def get_eyes(self):
			return self.__dict__.get('eyes', None)

	def set_eyes(self, eyes):
		self.__dict__['eyes'] = eyes
	
	def get_hairs(self):
		return self.__dict__.get('hairs', None)
	
	def set_hairs(self, hairs):
		self.__dict__['hairs'] = hairs

	eyes = property(get_eyes, set_eyes)
	hairs = property(get_hairs, set_hairs)
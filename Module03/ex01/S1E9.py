from abc import ABC, abstractmethod

class Character(ABC):
	def __init__(self, first_name, is_alive = True):
		"""Abstract class which  contains name and is_alive value"""
		self.first_name = first_name
		self.is_alive  = is_alive
	
	@abstractmethod
	def die(self):
		pass
		
class Stark(Character):
	"""Subclass for Character abstract class"""
	def change_value(self, first_name, is_alive):
		Stark.first_name = first_name
		Stark.is_alive = is_alive

	def die(self):
		"""Method that changes the state of the is_alive boolean"""
		self.is_alive = False

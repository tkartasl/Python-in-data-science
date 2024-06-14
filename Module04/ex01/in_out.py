def square(x: int | float) -> int | float:
	'''Function that returns square of the argument'''
	return x**2

def pow(x: int | float) -> int | float:
	'''Function that returns power of the argument'''
	return x**x

def outer(x: int | float, function) -> object:
	''' function that returns the square of argument, a function that returns the
	Exponentiation of argument by himself and a function that takes as argument a number
	and a function, it returns an object that when called returns the result of the arguments
	calculation.'''
	count = 0
	def inner() -> float:
		nonlocal x
		count = function(x)
		x = count
		return x
	return inner
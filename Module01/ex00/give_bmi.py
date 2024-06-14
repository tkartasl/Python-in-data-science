import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Function that receives two lists with weight and height and calculates bmi"""
	bmi = []

	np_height = np.array(height)
	np_weight = np.array(weight)
	try:
		assert len(height) == len(weight), "AssertionError: lists are not the same size"
		assert np_height.dtype in [np.float64, np.int64] and np_weight.dtype in [np.float64, np.int64], "AssertionError: list contents have to be integers or floats"
	except AssertionError as msg:
		print(msg)
		exit()
	for w, h in zip(np_weight, np_height):
		bmi.append(w / (h * h))
	return	bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""Function that checks is bmi is over a set limit and returns boolean"""
	res = []
	
	for i in bmi:
		if i > limit:
			res.append(True)
		else:
			res.append(False)
	return res

def main():
	"""Your function, give_bmi, take 2 lists of integers or floats in input and returns a list
	of BMI values.
	Your function, apply_limit, accepts a list of integers or floats and an integer representing
	a limit as parameters. It returns a list of booleans (True if above the limit)."""
	height = [1.60, 1.65, 1.70, 1.75, 1.80, 1.85]
	weight = [65, 75, 70, 70, 65, 105]
	bmi = give_bmi(height, weight)
	print(bmi, type(bmi))
	print(apply_limit(bmi, 26))
if __name__ == "__main__":
	main()
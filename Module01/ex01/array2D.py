import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""Function that takes as parameters a 2D array, prints its shape, and returns a
	truncated version of the array based on the provided start and end arguments."""
	try:
		assert all(len(row) == len(family[0]) for row in family), "AssertionError: lists has to  be the same size"
		assert family.__class__ == list, "AssertionError: type of first argument has to be list"
	except AssertionError as msg:
		print(msg)
		exit()
	arr = np.array(family)
	print('My shape is : ', np.shape(arr))
	ret = arr[start:end]
	print('My shape is : ', np.shape(ret))
	return ret.tolist()
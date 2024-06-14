import numpy as np
import array
from PIL import Image

def ft_load(path: str) -> array:
	"""Function that loads an image, prints its format, and its pixels
	content in RGB format."""
	try:
		im = Image.open(path)	
	except OSError:
		print("Failed to open image")
	arr = np.array(im)
	print('The shape of image is: ', np.shape(arr))
	return arr
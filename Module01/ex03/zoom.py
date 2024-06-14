#from load_image import ft_load
import numpy as np
import array
from PIL import Image

def ft_load(path: str) -> np.ndarray:
	"""Function that loads an image, prints its format, and its pixels
	content in RGB format."""
	try:
		im = Image.open(path)
	except OSError:
		print("Failed to open image")
		return None
	
	try:
		assert isinstance(path, str), "AssertionError: argument must be a string"
	except AssertionError as msg:
		print(msg)
		return None

	arr = np.array(im)
	print('The shape of image is: ', np.shape(arr))
	return arr

def zoom(arr: np.ndarray) -> np.ndarray:
	"""Program that should load the image "animal.jpeg", print some information
	about it and display it after "zooming"."""
	ret = arr[100:500, 400:800, 1]
	print('New shape after slicing: ', np.shape(ret))
	return ret

def main():
	"""main"""
	
	arr = ft_load("/home/tkartasl/Python_piscine/Module01/ex03/Animal.jpeg")
	if arr is None:
		return
	
	print(arr)
	res = zoom(arr)
	
	im = Image.fromarray(res.astype(np.uint8))
	im.show()

if __name__ == "__main__":
	main()
import pandas as pd

def load(path: str) -> pd.DataFrame:
	"""Function that takes a path as argument, writes the dimensions of the data set
	and returns it."""
	
	try:
		assert isinstance(path, str), "AssertionError: argument has to be string"
	except AssertionError as msg:
		print(msg)
		return None
	try:
		df = pd.read_csv(path)
		print('Loading dataframe of dimensions', df.shape)
		return df
	except FileNotFoundError:
		print(f"File not found: {path}")
		return None
	except pd.errors.EmptyDataError:
		print("File is empty")
		return None
	except pd.errors.ParserError:
		print("Error parsing the file")
		return None
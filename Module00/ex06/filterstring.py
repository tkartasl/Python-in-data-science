import sys
from ft_filter import ft_filter

def main():
	"""A program that accepts two arguments: a string(S), and an integer(N). The
program should output a list of words from S that have a length greater than N."""
	try:
		assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
		assert sys.argv[1].isprintable() == True, "AssertionError: the arguments are bad"
		assert sys.argv[2].isdigit() == True, "AssertionError: the arguments are bad"
	except AssertionError as msg:
		print(msg)
		exit()
	lst = sys.argv[1].split(" ")
	res = list(ft_filter(lambda lst: len(lst) > int(sys.argv[2]), lst))
	print(res)
if __name__ == "__main__":
	main()
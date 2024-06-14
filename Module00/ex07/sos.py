import sys

def main():
	"""Program that takes a string as an argument and encodes it into Morse Code."""

	nested_morse = {	" ": "/ ",
						"A": ".- ",
						"B": "-... ",
						"C": "-.-. ",
						"D": "-.. ",
						"E": ". ",
						"F": "..-. ",
						"G": "--. ",
						"H": ".... ",
						"I": ".. ",
						"J": ".--- ",
						"K": "-.- ",
						"L": ".-.. ",
						"M": "-- ",
						"N": "-. ",
						"O": "--- ",
						"P": ".--. ",
						"Q": "--.- ",
						"R": ".-. ",
						"S": "... ",
						"T": "- ",
						"U": "..- ",
						"V": "...- ",
						"W": ".-- ",
						"X": "-..- ",
						"Y": "-.-- ",
						"Z": "--.. ",
						"0": "----- ",
						"1": ".---- ",
						"2": "..--- ",
						"3": "...-- ",
						"4": "....- ",
						"5": "..... ",
						"6": "-.... ",
						"7": "--... ",
						"8": "---.. ",
						"9": "----. "
	}
	length = 0
	flag_punctuation = False
	for i in sys.argv[1]:
		if i in  "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
			flag_punctuation = True
	try:
		assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
		assert flag_punctuation == False, "AssertionError: the arguments are bad"
	except AssertionError as msg:
		print(msg)
		exit()
	input_inupper = sys.argv[1].upper()
	for i in input_inupper:
		if length == len(input_inupper) - 1:
			print(nested_morse.get(i).replace(" ", ""))
			break
		print(nested_morse.get(i), end = '')
		length += 1
if __name__ == "__main__":
	main()
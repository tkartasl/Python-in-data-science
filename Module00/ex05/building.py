# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:38:30 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/11 08:53:52 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def count_characters(string):
	upper = 0
	lower = 0
	punc = 0
	digit = 0
	space = 0
	chars = len(string)

	for i in string:
		if i.isupper() == True:
			upper += 1
		if i.islower() == True:
			lower += 1
		if i.isdigit() == True:
			digit += 1
		if i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
			punc += 1
		if i.isspace() == True:
			space += 1
	return [chars, upper, lower, punc, space, digit]

def main():
	"""Program that takes string as and input and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces."""

list = 0

try:
	assert len(sys.argv) <= 2 , "AssertionError: more than one argument is provided"
except AssertionError as msg:
	print(msg)
	exit()
if len(sys.argv) == 1:
	print('Provide a string as an argument')
	str = input()
else:
	str = sys.argv[1]
list = count_characters(str)
print('The text contains', list[0], 'characters:')
print(list[1], 'upper letters')
print(list[2], 'lower letters')
print(list[3], 'punctuation marks')
print(list[4], 'spaces')
print(list[5], 'digits')
if __name__ == "__main__":
	main()

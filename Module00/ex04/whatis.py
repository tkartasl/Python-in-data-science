# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:28:47 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/11 08:57:14 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
	assert sys.argv[1].lstrip('-').isdigit() == True, "AssertionError: argument has to be integer"
except AssertionError as msg:
	print(msg)
	exit()
if len(sys.argv) == 1:
	exit(0)
if int(sys.argv[1]) % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd")
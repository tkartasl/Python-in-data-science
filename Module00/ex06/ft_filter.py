# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 16:39:32 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/11 08:24:55 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_filter(function, iterable):
	"""Remake of the filter function"""
	if function is None:
		return iterable
	list = [x for x in iterable if function(x) is True]
	return list

def main():
	"""Remake of the filter function"""
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
#print(list(even_numbers))
if __name__ == "__main__":
	main()
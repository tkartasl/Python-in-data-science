# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 12:03:58 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/10 12:36:58 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if object.__class__ == list:
		print('List:', object.__class__)
	elif object.__class__ == tuple:
		print('Tuple:', object.__class__)
	elif object.__class__ == set:
		print('Set:', object.__class__)
	elif object.__class__ == dict:
		print('Dict:', object.__class__)
	elif object.__class__ == str:
		print(object, 'is in the kitchen : ', object.__class__)
	else:
		print("Type not found")
		return 42
	return 42
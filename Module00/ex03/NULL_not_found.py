# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 12:41:47 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/10 13:25:59 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	if object == None:
		print('Nothing: ', object, type(object))
		return 0
	elif object.__class__ == float:
		print('Cheese: ', object, type(object))
		return 0
	elif object.__class__ == int and object == 0:
		print('Zero: ', object, type(object))
		return 0
	elif object.__class__ == str and object is "":
		print('Empty: ', object, type(object))
		return 0
	elif object.__class__ == bool and object == False:
		print('Fake: ', object, type(object))
		return 0
	else:
		print('Type not found')
		return 1
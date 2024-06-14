# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 09:47:13 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/10 10:12:33 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World"
temp = list(ft_tuple)
temp[1] = "Finland"
ft_tuple = tuple(temp)
ft_set.remove("tutu!")
ft_set.add("Helsinki")
ft_dict["Hello"] = "Hive"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
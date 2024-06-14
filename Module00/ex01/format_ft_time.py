# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkartasl <tkartasl@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 09:46:27 by tkartasl          #+#    #+#              #
#    Updated: 2024/06/10 12:03:09 by tkartasl         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

print('Seconds since January 1, 1970: ', '{:,.2f}'.format(time.time()), 'or', "{:0.2e}".format(time.time()), 'in scientific notation')
print(datetime.today().strftime("%b %d %Y"))

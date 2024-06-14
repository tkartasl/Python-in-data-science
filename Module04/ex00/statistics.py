def ft_statistics(*args: any, **kwargs: any) -> None:
	"""You must take in *args a quantity of unknown number and make the Mean, Median,
	Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
	ask."""

	new_list = list(args)
	new_list.sort()

	def Mean(new_list):
		if len(new_list) == 0:
			print("ERROR")
			return None
		print(sum(new_list) / len(new_list))
	
	def Median(new_list):
		if len(new_list) == 0:
			print("ERROR")
			return
		index = int(len(new_list) / 2)
		if len(new_list) % 2 == 0:
			print('median : ', (new_list[index] + new_list[index -1]) / 2)
		else:
			print('median : ',new_list[index])

	def Quartile(new_list):
		if len(new_list) == 0:
			print("ERROR")
			return
		index = int(len(new_list)) / 2
		q_index = index / 2
		median = (new_list[int(index) - 1] + new_list[int(index)]) / 2
		if len(new_list) % 2 == 0:
			if index % 2 == 0:
				Q1 = (new_list[int(q_index)] + new_list[int(q_index) - 1]) / 2
				Q3 = (new_list[int(index + int(q_index))] + new_list[int(index + int(q_index) - 1)]) / 2
			else:
				Q1 = new_list[int(q_index)]
				Q3 = new_list[int(index) + int(q_index)]
		else:
			if int(index) % 2 == 0:
					Q1 = new_list[int(q_index)]
					Q3 = new_list[int(index) + int(q_index)]
			else:
				Q1 = (new_list[int(q_index)] + new_list[int(q_index) + 1]) / 2
				Q3 = (new_list[int(index) + int(q_index)] + new_list[int(int(index) + int(q_index) + 1)]) / 2
		print_list = [float(Q1), float(Q3)]	
		print('quartile : ', print_list)

	def Standard_Deviation(new_list):
		if len(new_list) == 0:
			print("ERROR")
			return
		variance_list = []
		mean = sum(new_list) / len(new_list)
		for i in new_list:
			variance_list.append((i - mean)**2)
		variance = sum(variance_list) / len(variance_list)
		print('std : ', variance**0.5)

	def Variance(new_list):
		if len(new_list) == 0:
			print("ERROR")
			return
		variance_list = []
		mean = sum(new_list) / len(new_list)
		for i in new_list:
			variance_list.append((i - mean)**2)
		variance = sum(variance_list) / len(variance_list)
		print('var : ', variance)

	for key, value in kwargs.items():
		if value == 'mean':
			Mean(new_list)
		elif value == 'median':
			Median(new_list)
		elif value == 'quartile':
			Quartile(new_list)
		elif value == 'std':
			Standard_Deviation(new_list)
		elif value == 'var':
			Variance(new_list)
def groups_of_3(values):
	newList = []

	for i in range(0, len(values)-2, 3):
		newList.append([values[i], values[i+1], values[i+2]])
	if len(values) % 3 == 2:
		newList.append([values[-2], values[-1]])
	elif len(values) % 3 == 1:
		newList.append([values[-1]])

	return newList

def groups_of_3(values):
	newList = []
	oldList = [i for x in values for i in x]				

	for i in range(0, len(oldList)-2, 3):
		newList.append([oldList[i], oldList[i+1], oldList[i+2]])
	if len(oldList) % 3 == 2:
		newList.append([oldList[-2], oldList[-1]])
	elif len(oldList) % 3 == 1:
		newList.append([oldList[-1]])

	return newList

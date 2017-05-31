import csv
def mesopy_to_csv(mesopy_ds, filename):
	matrix = [[]]
	#print(mesopy_ds)
	for key, values in mesopy_ds['STATION'][0]['OBSERVATIONS'].items():
		#print(key)
		try:
			matrix[0].append(key)
		except Exception:
			matrix.append(key)
		for index, value in enumerate(values, start=1):
			try:
				matrix[index].append(value)
			except Exception:
				temp=[]
				temp.append(value)
				matrix.append(temp)
	with open(filename, 'w', newline='') as csvfile:
		writer=csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(matrix)



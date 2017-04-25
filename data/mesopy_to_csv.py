def mesopy_to_csv(mesopy_ds):
	csv = [[]]
	#print(mesopy_ds)
	for key, values in mesopy_ds['STATION'][0]['OBSERVATIONS'].items():
		#print(key)
		try:
			csv[0].append(key)
		except Exception:
			csv.append(key)
		for index, value in enumerate(values, start=1):
			try:
				csv[index].append(value)
			except Exception:
				temp=[]
				temp.append(value)
				csv.append(temp)
	return csv


import csv

def get_coords(line): 

	return int(line[1]), int(line[2])

if __name__ == "__main__": 

	window_size = 10
	file_name = "test/test_set_sample.txt"
	
	with open(file_name) as f: 
		
		bed_file = csv.reader(f, delimiter='\t')

		line = next(bed_file)
		beginning, end = get_coords(line)
		region = [line]

		for line in bed_file: 
			# print(end - beginning)
			print("beginning: " + str(beginning))
			print("end: " + str(end))
			if end - beginning <= window_size: 
				region.append(line)
				region.append(["A"])
				_, end = get_coords(line)
			else: 
				# print(region)
				region = [line] 
				region.append(["E"])
				beginning, end = get_coords(line)
			print(region)










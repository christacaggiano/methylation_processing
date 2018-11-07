import csv

def get_coords(line): 
	return str(line[0]), int(line[1]), int(line[2])

def sum_counts(region): 
	counts = []
	for cpg in region: 
		counts.append([int(cpg[count]) for count in range(3, len(cpg), 2)])
	return [sum(x) for x in zip(*counts)]

def write_summed_counts(summed_counts, chrom, beginning, end, output): 
	output.writerow([chrom] + [beginning] + [end] + summed_counts)

if __name__ == "__main__": 

	window_size = 10
	file_name = "data/test_set_sample.txt"
	output_file = "data/test_summed.txt"
	
	with open(file_name, "r") as input_file, open(output_file, "w") as output_file: 
		
		bed_file = csv.reader(input_file, delimiter='\t')
		summed_file = csv.writer(output_file, delimiter='\t')

		line = next(bed_file)
		previous_chrom, beginning, end = get_coords(line)
		region = [line]

		for line in bed_file: 
		
			chrom, _, end = get_coords(line)

			if end - beginning <= window_size and chrom==previous_chrom: 
				region.append(line)
				previous_chrom = chrom
			else: 
				summed_counts = sum_counts(region)
				write_summed_counts(summed_counts, chrom, beginning, end, summed_file)
				region = [line] 
				chrom, beginning, _ = get_coords(line)









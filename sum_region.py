import csv
import numpy as np

def get_coords(line): 

	return str(line[0]), int(line[1]), int(line[2])


def sum_counts(region, output_file): 
	
	chrom = region[0][0]
	beginning = region[0][1]
	end = region[-1][2]

	number_of_cpgs = len(region)
	number_of_tissues = int((len(region[0]) - 3)/2) 

	count_matrix = np.empty((number_of_cpgs, number_of_tissues))

	# for cpg in region: 

	# 	counts, percents = get_counts_percents(cpg)
	# 	meth, unmeth = 
	# 	cpg_counts.append(counts)
	# 	cpg_percents.append(percent_meth)

	
	# write_summed_counts([sum(x) for x in zip(*counts)], chrom, beginning, end, output_file) 


def get_counts_percents(cpg): 

	counts = np.array([int(cpg[count]) for count in range(3, len(cpg), 2)])
	percents = np.array([float(cpg[count])/100 for count in range(4, len(cpg), 2)])

	return counts, percents


def get_methylation(counts, percents):

	number_methylated = counts*percents
	number_unmethylated = counts-number_methylated

	# percent_methylated = 
	
	return percent_methylated

# def sum_counts(cpg_counts, cpg_percents): 

# 	summed_counts = [sum(x) for x in zip(*counts)]


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
				sum_counts(region, summed_file)
				region = [line] 
				previous_chrom, beginning, _ = get_coords(line)

		sum_counts(region, summed_file)







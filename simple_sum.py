import csv
import numpy as np
import pandas as pd
import sys

BATCH_SIZE = 100
FILTER_PARAMETER = 0

def get_coords(line): 

	return str(line[0]), int(line[1]), int(line[2])


def define_region(region): 

	chrom = region[0][0]
	beginning = region[0][1]
	end = region[-1][2]

	return [chrom, beginning, end]


def collapse_region(region): 
	
	values = [x[3:] for x in region]
	
	values_corrected = []
	for l in values: 
		new_list = []
		for item in l: 
			if item=="NA": 
				new_list.append(0)
			else: 
				new_list.append(item)
		values_corrected.append(new_list)

	values_array = np.array(values_corrected, dtype=float)
	
	summed = values_array.sum(axis=0)
	
	return summed.tolist()


def update_counts(summed_counts, row): 
	
	summed_counts += np.array([int(c) for c in row[3:]])
	 
def get_summed_percents(methylated, unmethylated): 

	methylated_summed = np.sum(methylated, axis=0)
	unmethylated_summed = np.sum(unmethylated, axis=0)

	total = methylated_summed + unmethylated_summed
	total[total == 0] = np.nan

	return methylated_summed / total, total 


def write_summed_file(summed_sites, output): 
	
	output.writerows(summed_sites) 


if __name__ == "__main__": 

	window_size = int(sys.argv[1])
	file_name = sys.argv[2]
	counts_output_file = sys.argv[3]

	print(window_size)
	
	with open(file_name, "r") as input_file, open(counts_output_file, "w") as counts_output_file: 
		
		bed_file = csv.reader(input_file, delimiter='\t')
		summed_file_counts = csv.writer(counts_output_file, delimiter='\t')

		line = next(bed_file)
		previous_chrom, beginning, end = get_coords(line)
		region = [line]

		summed_regions_counts = []

		for line in bed_file: 
			# print(line)
		
			chrom, _, end = get_coords(line)
			

			if end - beginning <= window_size and chrom==previous_chrom: 
				region.append(line)
				previous_chrom = chrom
			else: 
				
				new_region = collapse_region(region)

				summed_line = [chrom, beginning, end] + new_region
				summed_regions_counts.append(summed_line)
				
				region = [line] 
				previous_chrom, beginning, _ = get_coords(line)

			if len(summed_regions_counts)>BATCH_SIZE:
				
				write_summed_file(summed_regions_counts, summed_file_counts)
				summed_regions_counts.clear()

				
		write_summed_file(summed_regions_counts, summed_file_counts)







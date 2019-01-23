import csv
import numpy as np
import pandas as pd
import sys

BATCH_SIZE = 10000
FILTER_PARAMETER = 75

def get_coords(line): 

	return str(line[0]), int(line[1]), int(line[2])


def define_region(region): 

	chrom = region[0][0]
	beginning = region[0][1]
	end = region[-1][2]

	return [chrom, beginning, end]


def collapse_region(region, output_file): 

	print(region)
	# return define_region(region) + percents.tolist(), total_reads

def write_summed_file(summed_sites, output): 
	
	output.writerows(summed_sites) 


if __name__ == "__main__": 

	sys.argv[1]
	window_size = int(sys.argv[1])
	file_name = sys.argv[2]
	output_file = sys.argv[3]
	
	with open(file_name, "r") as input_file, open(output_file, "w") as output_file: 
		
		bed_file = csv.reader(input_file, delimiter='\t')
		summed_file = csv.writer(output_file, delimiter='\t')
		
		line = next(bed_file)
		previous_chrom, beginning, end = get_coords(line)
		region = [line]
		summed_regions = []

		for line in bed_file: 
		
			chrom, _, end = get_coords(line)

			if end - beginning <= window_size and chrom==previous_chrom: 
				region.append(line)
				previous_chrom = chrom
			else: 
				summed, total_reads = collapse_region(region, summed_file)
				if total_reads > FILTER_PARAMETER: 
					summed_regions.append(summed)
				region = [line] 
				previous_chrom, beginning, _ = get_coords(line)

			if len(summed_regions)>BATCH_SIZE:
				write_summed_file(summed_regions, summed_file)
				summed_regions.clear()

				
		write_summed_file(summed_regions, summed_file)






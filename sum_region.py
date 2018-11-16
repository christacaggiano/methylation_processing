import csv
import numpy as np
import pandas as pd


def get_coords(line): 

	return str(line[0]), int(line[1]), int(line[2])


def define_region(region): 

	chrom = region[0][0]
	beginning = region[0][1]
	end = region[-1][2]

	return [chrom, beginning, end]


def collapse_region(region, output_file): 

	num_cpgs = len(region)
	num_tissues = int((len(region[0]) - 3)/2) 

	methylated = np.empty((num_cpgs, num_tissues))
	unmethylated = np.empty((num_cpgs, num_tissues))

	for row, cpg in enumerate(region): 
		update_counts(cpg, methylated, unmethylated, row)
	
	summed = get_summed_percents(methylated, unmethylated)
	mean, std = get_correlation(summed)

	return define_region(region) + [mean] + [std]


def update_counts(cpg, methylated, unmethylated, index): 
	
	counts = np.array([int(cpg[count]) for count in range(3, len(cpg), 2)])
	percents = np.array([float(cpg[count])/100 for count in range(4, len(cpg), 2)])

	number_methylated = counts*percents
	number_unmethylated = counts-number_methylated

	methylated[index] = number_methylated
	unmethylated[index] = number_unmethylated


def get_summed_percents(methylated, unmethylated): 

	total = methylated + unmethylated
	total[total == 0] = np.nan

	return methylated/total


def get_correlation(summed_percents):
	
	df = pd.DataFrame(summed_percents.T)
	corr = df.corr(method='pearson')
		
	return average_pairwise_correlation(corr) 
	

def average_pairwise_correlation(corr):

	lower = corr.mask(np.triu(np.ones(corr.shape)).astype(bool)).stack()

	return lower.mean(), lower.std()
	

def write_summed_file(summed_sites, output): 
	
	for cpg in summed_sites:
		output.writerow(cpg) 


if __name__ == "__main__": 

	window_size = 1000
	file_name = "../test/test_data.txt"
	output_file = "data/test_summed.txt"
	
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
				summed_regions.append(collapse_region(region, summed_file))
				region = [line] 
				previous_chrom, beginning, _ = get_coords(line)
				
		write_summed_file(summed_regions, summed_file)






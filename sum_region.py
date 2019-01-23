import csv
import numpy as np
import pandas as pd
import sys

BATCH_SIZE = 1000
FILTER_PARAMETER = 200

def get_coords(line): 

	return str(line[0]), int(line[1]), int(line[2])


def define_region(region): 

	chrom = region[0][0]
	beginning = region[0][1]
	end = region[-1][2]

	return [chrom, beginning, end]


def collapse_region(region): 

	num_cpgs = len(region)
	num_tissues = int((len(region[0]) - 3)/2) 

	methylated = np.empty((num_cpgs, num_tissues))
	unmethylated = np.empty((num_cpgs, num_tissues))

	for row, cpg in enumerate(region): 
		update_counts(cpg, methylated, unmethylated, row)
	
	# percents = get_percents(methylated, unmethylated)
	# mean, std = get_correlation(percents)
	percents, total_reads = get_summed_percents(methylated, unmethylated)
	return define_region(region) + percents.tolist(), total_reads


def update_counts(cpg, methylated, unmethylated, index): 
	
	counts = np.array([float(cpg[count]) if not cpg[count] == "" else np.nan for count in range(3, len(cpg), 2)])
	percents = np.array([float(cpg[count])/100  if not cpg[count] == "" else np.nan for count in range(4, len(cpg), 2)])

	number_methylated = counts*percents
	number_unmethylated = counts-number_methylated

	methylated[index] = number_methylated
	unmethylated[index] = number_unmethylated


def get_percents(methylated, unmethylated): 

	total = methylated + unmethylated
	total[total == 0] = np.nan

	return methylated/total

def get_summed_percents(methylated, unmethylated): 

	methylated_summed = np.sum(methylated, axis=0)
	unmethylated_summed = np.sum(unmethylated, axis=0)

	total = methylated_summed + unmethylated_summed
	total[total == 0] = np.nan

	return methylated_summed / total, total 

def get_correlation(summed_percents):
	
	df = pd.DataFrame(summed_percents.T)
	corr = df.corr(method='pearson')
		
	return average_pairwise_correlation(corr) 
	

def average_pairwise_correlation(corr):

	lower = corr.mask(np.triu(np.ones(corr.shape)).astype(bool)).stack()

	return lower.mean(), lower.std()
	

def write_summed_file(summed_sites, output): 
	
	output.writerows(summed_sites) 


if __name__ == "__main__": 

	window_size = int(sys.argv[1])
	file_name = sys.argv[2]
	percents_output_file = sys.argv[3]
	counts_output_file = sys.argv[4]
	
	with open(file_name, "r") as input_file, open(counts_output_file, "w") as counts_output_file, open(percents_output_file, "w") as percents_output_file: 
		
		bed_file = csv.reader(input_file, delimiter='\t')
		summed_file_percents = csv.writer(percents_output_file, delimiter='\t')
		summed_file_counts = csv.writer(counts_output_file, delimiter='\t')

		line = next(bed_file)
		previous_chrom, beginning, end = get_coords(line)
		region = [line]
		summed_regions_percents = []
		summed_regions_counts = []

		for line in bed_file: 
		
			chrom, _, end = get_coords(line)

			if end - beginning <= window_size and chrom==previous_chrom: 
			
				region.append(line)
				previous_chrom = chrom
			else: 
				summed, total_counts = collapse_region(region)

				if np.nansum(total_counts) > FILTER_PARAMETER: 

					summed_regions_percents.append(summed)
					summed_regions_counts.append(total_counts)

				region = [line] 
				previous_chrom, beginning, _ = get_coords(line)

			if len(summed_regions_percents)>BATCH_SIZE:
				write_summed_file(summed_regions_percents, summed_file_percents)
				write_summed_file(summed_regions_counts, summed_file_counts)

				summed_regions_counts.clear()
				summed_regions_percents.clear()

				
		write_summed_file(summed_regions_percents, summed_file_percents)
		write_summed_file(summed_regions_counts, summed_file_counts)







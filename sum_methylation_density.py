import csv
import numpy as np
import pandas as pd
import sys
import collections


def get_region_dict(file): 

	regions_dict = collections.defaultdict(list)

	with open(file, "r") as input_file: 
		list_file = csv.reader(input_file, delimiter="\t")

		for line in list_file: 
			chrom, start, end = line[0], line[1], line[2]
			regions_dict[chrom].append({"start":int(start), "end":int(end), "meth":0, "unmeth":0, "total_cpgs":0})

	return regions_dict


def get_methylation_counts(file, regions_dict): 
	with open(file, "r") as input_file: 
		cpg_file = csv.reader(input_file, delimiter="\t")

		for line in cpg_file: 
			chrom, start, end, meth, unmeth = line 
			
			if chrom in regions_dict: 
				for region in regions_dict[chrom]: 
					if int(start) >= region["start"] and int(end) <= region["end"]: 
						region["meth"] += float(meth)
						region["unmeth"] += float(unmeth)
						region["total_cpgs"] += 1
						
	return regions_dict		


def write_bed_file(output_file, regions_dict): 
	with open(output_file, "w") as output: 
		bed_file = csv.writer(output, delimiter="\t")

		for chrom in regions_dict: 
			for region in regions_dict[chrom]:
				bed_file.writerow([chrom] + [region["start"]] + [region["end"]] + [region["meth"]] + [region["unmeth"]])
		
if __name__ == "__main__": 

	list_file = sys.argv[1]
	tissue_cpg_file = sys.argv[2]
	output_file_name = sys.argv[3]
	
	regions = get_region_dict(list_file)
	get_methylation_counts(tissue_cpg_file, regions)
	write_bed_file(output_file_name, regions)


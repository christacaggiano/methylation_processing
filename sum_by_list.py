import csv
import numpy as np
import pandas as pd
import sys
import collections


def get_region_dict(file): 

	regions = defaultdict(list)

	with open(file, "r") as input_file: 
		list_file = csv.reader(input_file, delimiter="\t")

		for line in list_file: 
			chrom, start, end = line[0], line[1], line[2]
			regions[chrom].append({"start":start, "end":end, "meth":0, "unmeth":0})

	return regions
		
		
if __name__ == "__main__": 

	list_file = sys.argv[1]
	input_file_name = sys.argv[2]
	output_file_name = sys.argv[3]
	
	print(get_region_dict(file))

	# with open(list_file, "r") as lf, open(input_file_name, "r") as i, open(output_file_name, "w") as o: 
		
	# 	list_file = csv.reader(lf, delimiter='\t')
	# 	input_file = csv.writer(i, delimiter='\t')

	# 	output_file = csv.writer(o, delimiter='\t')




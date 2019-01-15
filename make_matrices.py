import numpy as np
import csv

def get_counts(line): 
	
	counts = np.array([int(x) for x in line[23::2]])
	percents = np.array([float(x)/100 for x in line[24::2]])
	number_methylated = counts*percents.round(0)
	number_unmethylated = counts-number_methylated

	return percents, number_methylated, number_unmethylated


if __name__ == "__main__": 

	meth_file = "training_roadmap_tss_meth.txt"
	unmeth_file = "training_roadmap_tss_unmeth.txt"
	percent_file = "training_roadmap_tss_percents.txt"
	input_file = "training_roadmap_tss.txt"

	with open(input_file, "r") as f, open(unmeth_file, "w") as unmeth_out, open(meth_file, "w") as meth_out, open(percent_file, "w") as percent_out: 

		test = csv.reader(f, delimiter="\t")
		percent_out = csv.writer(percent_out, delimiter="\t")
		meth_out = csv.writer(meth_out, delimiter="\t")
		unmeth_out = csv.writer(unmeth_out, delimiter="\t")

		for line in test: 
	
			percents, meth, unmeth = get_counts(line)
			
			percent_out.writerow(line[20:23] + percents.tolist())
			meth_out.writerow(meth.tolist()) 
			unmeth_out.writerow(unmeth.tolist())

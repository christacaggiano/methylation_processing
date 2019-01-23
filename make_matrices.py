import numpy as np
import csv

def get_counts(percents, counts): 
	
	counts = np.array([float(x) if x is not "." else np.nan for x in counts])
	percents = np.array([float(x) if x is not "." else np.nan for x in percents[3:]])

	number_methylated = counts*percents
	number_unmethylated = counts-number_methylated

	return percents, number_methylated, number_unmethylated


if __name__ == "__main__": 

	meth_file = "data/training_tss_meth.txt"
	unmeth_file = "data/training_tss_unmeth.txt"
	percent_file = "data/training_roadmap_tss_percents.txt"
	percent_file_input = "data/training_tss_percents.txt"
	count_file_input = "data/training_tss_counts.txt"

	with open(percent_file_input, "r") as f1, open(count_file_input, "r") as f2, open(unmeth_file, "w") as unmeth_out, open(meth_file, "w") as meth_out, open(percent_file, "w") as percent_out: 

		percent_in = csv.reader(f1, delimiter="\t")
		count_in = csv.reader(f2, delimiter="\t")
		percent_out = csv.writer(percent_out, delimiter="\t")
		meth_out = csv.writer(meth_out, delimiter="\t")
		unmeth_out = csv.writer(unmeth_out, delimiter="\t")

		for p, c in zip(percent_in, count_in): 
	
			percents, meth, unmeth = get_counts(p, c)
		
			percent_out.writerow(p + percents.tolist())
			meth_out.writerow(meth.tolist()) 
			unmeth_out.writerow(unmeth.tolist())

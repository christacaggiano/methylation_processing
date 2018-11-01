import numpy as np
import csv

with open("test_data_nocounts.txt", "r") as f, open("training_with_var.txt", "w") as out: 

	output = csv.writer(out, delimiter=" ")

	for line in f: 
		split_line = line.strip("\n").strip(" ").split(" ")
		percents = [float(x)/100 for x in split_line[2:]]

		var = np.nanvar(percents)

		output.writerow(split_line[:2] + percents + [np.around(var, 4)]) 
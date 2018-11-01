import csv
with open("training_data_nocounts.bed") as in_file, open("training_data_nocounts_filtered.bed", "w") as out:
	out_csv = csv.writer(out, delimiter="\t")
	for line in in_file:

		chrom_numbers = list(range(1, 22)) + ["X", "Y"]
		allowed_chroms = ["chr" + str(i) for i in chrom_numbers]

		start = line.split()[0]
		if start in allowed_chroms: 

			out_csv.writerow(line.split())

		

import csv
with open("test_top_var_sites.bed") as in_file, open("test_top_var_sites.bed.txt", "w") as out:
	out_csv = csv.writer(out, delimiter="\t")
	for line in in_file:
		line = line.split()
		newcolumn = int(line[1])-2
		out_csv.writerow(line[:1]+[newcolumn]+line[1:])

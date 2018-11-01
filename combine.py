import csv	
import sys	
	
def make_cpg_set(cpg_file):	
	
	cpgs = []	
	
	with open(cpg_file, "r") as f: 	
		for line in f: 	
			if len(line.split("\t")) > 1: 
				chrom, start, end = line.strip("\n").split("\t")[0:3]	
	
				cpgs.append((chrom, int(start)))
		
	return cpgs 	
	
	
def cache_list(lines, new_item, size):	
    if len(lines)>size:	
        lines.pop(0)	
    lines.append(new_item.strip("\n").split("\t"))	
    	
	
def select_cpgs(reference_file, cpgs, surround, output_file): 	
	
	with open(reference_file, "r") as f, open(output_file, "w") as out: 	
		output = csv.writer(out, delimiter="\t")	
			
		counter=0		
		previous = []	
	
		for line in f:	
			chrom, start, end = line.split("\t")[0:3]
			start = int(start) 
			cache_list(previous, line, surround)	
			if (chrom, start) in cpgs:
				print("in")
				output.writerow(line.strip("\n").split("\t"))	


			# 	counter = surround	
			# 	for l in previous: 	
			# 		output.writerow(l)	
	
			# if counter>0:	
			# 	output.writerow(line.strip("\n").split("\t"))	
			# 	counter -= 1	
	
def read_file_names(file): 	
	
	names = []	
	
	with open(file) as f: 	
		for line in f: 	
			names.append(line.strip("\n"))	
	
	return names	
	
	
	
if __name__ == "__main__": 	
	
	# file_number = int(sys.argv[1]) - 1 	
	# surround_number = int(sys.argv[2])
	surround_number = 1

	# file_names = read_file_names("file_names.txt")	
	file = "test.new.txt"
	
	cpg_set = make_cpg_set("training_top_var_sites.bed")

	print(cpg_set)
		
	# file = str(file_names[file_number]) 	
	# output = "muscle/" + file.split(".")[0] + ".surround_" + str(surround_number) + ".txt"	
	# output = "training_data_nocounts.bed_surround"
	
	# select_cpgs(file, cpg_set, surround_number, output)	
	
	
	

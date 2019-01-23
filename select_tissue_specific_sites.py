import csv
import numpy as np 

def get_counts(percents, counts): 
    
    percents = np.array([float(x) for x in percents[3:]])
    counts = np.array([float(x) for x in counts])

    number_methylated = counts * percents
    
    number_unmethylated = counts - number_methylated

    return percents.tolist(), number_methylated.tolist(), number_unmethylated.tolist(), counts.tolist()


def check_site(values, tissue_index, leuk_index): 
    percents = make_proportions(values) 
    
    if percents[tissue_index] < 0.5 and percents[leuk_index] >= 0.9:
    # if percents[tissue_index] < 0.5:

        if test_hypermethylated(percents, tissue_index, leuk_index): 
            return percents 
        

def make_proportions(values): 
    # percents = get_percents(values)
    return [float(val) for val in values] 


def get_percents(values): 
    return values[4::2]


def get_other_tissues(percents, tissue_index, leuk_index):
    return [x for i, x in enumerate(percents) if i not in [tissue_index, leuk_index]]


def test_hypermethylated(percents, tissue_index, leuk_index): 
    other_tissues = get_other_tissues(percents, tissue_index, leuk_index)
    hypermethylated = [x for x in other_tissues if x > 0.8] 

    return len(hypermethylated)/len(other_tissues) > 0.7 


if __name__ == "__main__": 

    methylation_file = "data/small_ref_merged_1000_percents.txt" 
    counts_file = "data/small_ref_merged_1000_counts.txt"
    
    output_percents = "data/small_ref_tss_percents_lessstrict.txt"
    output_meth = "data/small_ref_tss_meth_lessstrict.txt"
    output_unmeth = "data/small_ref_tss_unmeth_lessstrict.txt"

    with open(methylation_file, "r") as f1, open(counts_file, "r") as f2, open(output_percents, "w") as f3, open(output_meth, "w") as f4, open(output_unmeth, "w") as f5:
        percents_reader = csv.reader(f1, delimiter="\t")
        counts_reader = csv.reader(f2, delimiter="\t")

        percent_writer = csv.writer(f3, delimiter="\t")
        meth_writer = csv.writer(f4, delimiter="\t")
        unmeth_writer = csv.writer(f5, delimiter="\t")

        for p, c in zip(percents_reader, counts_reader):
            percents, meth, unmeth, counts = get_counts(p, c)

            sites = [] 

            for i, val in enumerate(percents):
                if counts[i] > 0: 
                    site = check_site(percents, i, -6)

                    if site:
                        sites.append((site, i)) 
                   
            if len(sites) == 1:
                percent_writer.writerow(p[:3] + sites[0][0] + ["tissue:" + str(sites[0][1])])
                meth_writer.writerow(meth)
                unmeth_writer.writerow(unmeth)
             



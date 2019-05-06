import csv
import numpy as np 

def get_counts(percents): 
    
    percents = np.array([float(x) if not x == "NA" else np.nan for x in percents[3:]])

    return percents.tolist()


def check_site(percents, tissue_index, leuk_index): 
    # percents = make_proportions(values) 
    
    if percents[tissue_index] < 0.5 and percents[leuk_index] >= 0.9:

        if test_hypermethylated(percents, tissue_index, leuk_index): 
            return percents 



def get_other_tissues(percents, tissue_index, leuk_index):
    return [x for i, x in enumerate(percents) if i not in [tissue_index, leuk_index]]


def test_hypermethylated(percents, tissue_index, leuk_index): 
    other_tissues = get_other_tissues(percents, tissue_index, leuk_index)
    hypermethylated = [x for x in other_tissues if x > 0.9] 

    return len(hypermethylated)/len(other_tissues) > 0.8 


if __name__ == "__main__": 

    methylation_file = "../../chip-reference-matrix/large_hg38_na.txt" 
    
    output_percents = "data/large_hg38_na_tss.txt" 
    
    with open(methylation_file, "r") as f1, open(output_percents, "w") as f3:
        percents_reader = csv.reader(f1, delimiter="\t")
        percent_writer = csv.writer(f3, delimiter="\t")

        for p in percents_reader:
            percents = get_counts(p)

            sites = [] 

            for i, val in enumerate(percents):
                site = check_site(percents, i, -1)

                if site:
                    sites.append((site, i)) 
                   
            if len(sites) == 1:
                percent_writer.writerow(p[:3] + sites[0][0] + ["tissue:" + str(sites[0][1])])
             



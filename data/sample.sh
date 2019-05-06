#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=40G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=20G,scratch=20G         	
#$ -l h_rt=72:00:00 	

conda activate py36	

# cat small_ref_merged_10_percents.txt | awk 'BEGIN {srand()} !/^$/ { if (rand() <= .01) print $0}' > sample.txt
# cat test_summed_1000_redone.txt | awk 'BEGIN {srand()} !/^$/ { if (rand() <= .01) print $0}' > test_summed_1000_sample.txt
# bedtools intersect -a test_summed_1000_sample.txt -b test_summed_1000_redone_counts_sites.txt -wb > test_summed_1000_counts_sample.txt
cat test_summed_100_redone.txt | awk 'BEGIN {srand()} !/^$/ { if (rand() <= .01) print $0}' > test_summed_100_sample.txt
bedtools intersect -a test_summed_100_sample.txt -b test_summed_100_redone_counts_sites.txt -wb > test_summed_100_counts_sample.txt
cat test_summed_100_redone.txt | awk 'BEGIN {srand()} !/^$/ { if (rand() <= .01) print $0}' > test_summed_100_sample2.txt
bedtools intersect -a test_summed_100_sample2.txt -b test_summed_100_redone_counts_sites.txt -wb > test_summed_100_counts_sample2.txt

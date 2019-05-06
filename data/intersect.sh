#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=30G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=20G,scratch=20G         	
#$ -l h_rt=72:00:00 	

conda activate py36	

# bedtools intersect -a test_summed_1000_counts_sample.txt -b training_summed_1000_redone_counts_sites.txt -wb > test_training_1000_counts.txt
# bedtools intersect -a test_training_1000_counts.txt -b training_summed_1000_redone.txt -wb > test_training_1000_counts_percents.txt
bedtools intersect -a test_summed_100_counts_sample.txt -b training_summed_100_redone_counts_sites.txt -wb > test_training_1000_counts.txt

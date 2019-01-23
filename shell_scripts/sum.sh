#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=10G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=10G,scratch=10G         	
#$ -l h_rt=72:00:00 	

conda activate py36	

cd ../
# python sum_region.py 1000 ../test/output_sites.txt data/test_summed_1000_redone.txt data/test_summed_1000_redone_counts.txt
# python sum_region.py 1000 ../training/output_sites.txt data/training_summed_1000_redone.txt data/training_summed_1000_redone_counts.txt
python simple_sum.py 500 ../../../primary_methylation_data_ALS/processed/merged_1-24_meth.txt ../../../primary_methylation_data_ALS/processed/merged_1-24_meth_500.txt
python simple_sum.py 500 ../../../primary_methylation_data_ALS/processed/merged_1-24_unmeth.txt ../../../primary_methylation_data_ALS/processed/merged_1-24_unmeth_500.txt
#python sum_region.py 1000 ../../encode/small_ref_merged.txt data/small_ref_merged_1000_percents.txt data/small_ref_merged_1000_counts.txt
#python sum_region.py 10000 ../../encode/small_ref_merged.txt data/small_ref_merged_10000_percents.txt data/small_ref_merged_10000_counts.txt

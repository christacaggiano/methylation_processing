#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=5G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=10G,scratch=10G         	
#$ -l h_rt=72:00:00 	

conda activate py36	

cd ../
python sum_region.py 1000 ../test/output_sites.txt data/test_summed_1000_redone.txt data/test_summed_1000_redone_counts.txt
python sum_region.py 1000 ../training/output_sites.txt data/training_summed_1000_redone.txt data/training_summed_1000_redone_counts.txt

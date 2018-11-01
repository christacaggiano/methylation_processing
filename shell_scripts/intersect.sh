#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=8G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=5G,scratch=5G         	
#$ -l h_rt=72:00:00 	
#$ -t 1
	
# bedtools intersect -a test_data_nocounts_filtered.bed -b training_top_var_sites.bed -loj > test_top_var_sites.bed
bedtools intersect -a training_top_var_sites_updated.txt -b training_data_nocounts_filtered.bed  -loj > test_top_var_redone.txt

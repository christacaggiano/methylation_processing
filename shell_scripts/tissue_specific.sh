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
python select_tissue_specific_sites.py
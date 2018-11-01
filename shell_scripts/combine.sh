#!/bin/bash                         	
	
#$ -S /bin/bash                     	
#$ -cwd                            	
#$ -r y                            	
#$ -j y                           	
#$ -l mem_free=2G                 	
#$ -l arch=linux-x64               	
#$ -l netapp=5G,scratch=5G         	
#$ -l h_rt=72:00:00 	
#$ -t 1
	
python combine.py $SGE_TASK_ID 12

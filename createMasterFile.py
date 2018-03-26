import os
import csv

def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,STATION, LINENAME, DIVISION, DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
        	fileData = open(filename, "r")
        	numberLine = 0
        	for line in fileData.readlines():
        		if numberLine != 0:
        			master_file.write(line)
        		numberLine += 1
        	fileData.close()

directory = "data"
master_file = "masterfile.csv"
completeFiles = list()
filenames = os.listdir(directory)

for file in filenames:
	completeFile = "%s/%s" % (directory, file)
	completeFiles.append(completeFile)

create_master_turnstile_file(completeFiles, "masterfile.csv")


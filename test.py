'''
Author: Rodrigo Luzuriaga
Date started: 01/04/2017
Date last modified: 01/06/2017

This script was created to clean up an external hard drive with data scattered all over the place.
The user, in this file, specifies the directory to where all the files are located and then creates folders for the
    file extension of all the files in the directory and all the sub-directories.
The program then copies or moves the files into the new directory that the program made for those specific files.
'''

import os
import shutil

search_directory = '/home/ubuntu/workspace/testdir'

clean_directory = '/home/ubuntu/workspace/clean/'

map_file_path = "/home/ubuntu/workspace/clean/map.txt"

map_file_write = open(map_file_path, 'w')

for folderName, subFolders, fileNames in os.walk(search_directory):
    for fileName in fileNames:
        if folderName == clean_directory:
            pass
        else:
            map_file_write.write(folderName + "/" + fileName + "\n")

map_file_write.close()


map_file_read = open(map_file_path, 'r')


for line in map_file_read:
    line = line.strip("\n")
# TODO: Need to make sure that if there are multiple files with the same name that they get changed so that it doesn't overwrite the files
    if line[-3] == ".":
        destination_path = clean_directory + line[-2:]
        
    elif line[-4] == ".":
        destination_path = clean_directory + line[-3:]
    elif line[-5] == ".":
        destination_path = clean_directory + line[-4:]
    
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    shutil.copy2(line, destination_path)
    

map_file_read.close()




"""
for line in map_file_read:
    line = line.strip("\n")
# TODO: Need to make sure that if there are multiple files with the same name that they get changed so that it doesn't overwrite the files
    if line[-3] == ".":
        if not os.path.exists(clean_directory + line[-2:]):
            os.makedirs(clean_directory + line[-2:])
            shutil.copy(line, clean_directory + line[-2:])
        else:
            shutil.copy(line, clean_directory + line[-2:])
    
    if line[-4] == ".":
        if not os.path.exists(clean_directory + line[-3:]):
            os.makedirs(clean_directory + line[-3:])
            shutil.copy(line, clean_directory + line[-3:])
        else:
            shutil.copy(line, clean_directory + line[-3:])
    
    if line[-5] == ".":
        if not os.path.exists(clean_directory + line[-4:]):
            os.makedirs(clean_directory + line[-4:])
            shutil.copy(line, clean_directory + line[-4:])
        else:
            shutil.copy(line, clean_directory + line[-4:])


for folderName, subFolders, fileNames in os.walk('/home/pi/Desktop/'):
	for subFolder in subFolders:
		for fileName in fileNames:
			print("folder name: " + folderName)
			print("sub folder " + subFolder)
			print("file name " + fileName)
			print('')
			if fileName[-4:] == ".jpg":
				print("folder name: " + folderName)
				print("sub folder: " + subFolder)
				source_path = folderName + fileName
				destination_path = "/home/pi/jpg"
				print("source: " + source_path)
				print("Destination " + destination_path)
				shutil.copy(source_path, destination_path)
			elif fileName[-4:] == ".mp3":
				source_path = folderName + fileName
				destination_path = "/home/pi/mp3"
				shutil.copy(source_path, destination_path)
			elif fileName[-4:] == ".png":
				source_path = folderName + fileName
				destination_path = "/home/pi/png"
				shutil.copy(source_path, destination_path)



        for subFolder in subFolders:
            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    print("folder name: " + folderName)
                    print("sub folder: " + subFolder)
                    source_path = "/home/pi/Desktop/" + subFolder + fileName
                    destination_path = "/home/pi/jpg"
                    print("source: " + source_path)
                    print("Destination " + destination_path)
                    shutil.copy(source_path, destination_path)
                elif fileName[-4:] == ".mp3":
                    source_path = folderName + fileName
                    destination_path = "/home/pi/mp3"
                    shutil.copy(source_path, destination_path)
                elif fileName[-4:] == ".png":
                    source_path = folderName + fileName
                    destination_path = "/home/pi/png"
                    shutil.copy(source_path, destination_path)
"""

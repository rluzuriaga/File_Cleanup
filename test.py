'''
Author: Rodrigo Luzuriaga
Date started: 01/04/2017
Date last modified: 01/25/2017

This script was created to clean up an external hard drive with data scattered all over the place.
The user, in this file, specifies the directory to where all the files are located and then creates folders for the
    file extension of all the files in the directory and all the sub-directories.
The program then copies or moves the files into the new directory that the program made for those specific files.
'''

import os
import shutil
from time import sleep

search_directory = '/home/ubuntu/workspace/testdir'  # This is the directory that you want to read from. Only change what is inside the ' '

clean_directory = '/home/ubuntu/workspace/clean/'  # This is the directory that you want to move the files to. In this directory the script will create all the necesary folders and copy over the files

map_file_path = "/home/ubuntu/workspace/clean/map.txt"











###########################################################################################################################################################################
###########################################################################################################################################################################
## 
### DO NOT CHANGE ANYTHING BELLOW UNLESS YOU KNOW WHAT YOU ARE DOING
##
###########################################################################################################################################################################
###########################################################################################################################################################################











full_name_list = []

file_name_list = []

map_file_write = open(map_file_path, 'w')
file_names_write = open("/home/ubuntu/workspace/clean/fileNames.txt", 'w')

for folderName, subFolders, fileNames in os.walk(search_directory):
    for fileName in fileNames:
        if folderName == clean_directory:
            pass
        else:
            map_file_write.write(folderName + "/" + fileName + "\n")
            file_names_write.write(fileName + "\n")
            
            # Append to two lists with folderName+fileName and just fileName
            full_name_list.append(folderName + "/")
            file_name_list.append(fileName)
            

map_file_write.close()



for full_path, file_name in zip(full_name_list, file_name_list):
    i = 0
    
    if file_name[-3] == ".":
        destination_path = clean_directory + file_name[-2:]
    elif file_name[-4] == ".":
        destination_path = clean_directory + file_name[-3:]
    elif file_name[-5] == ".":
        destination_path = clean_directory + file_name[-4:]
    
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    
    def file_renamer(file_name, i):
        file_name_no_ext = file_name.split(".", 1)[0]  # Creates the variable that only holds the file name without the file extension
        file_name_ext = file_name.split(".", 1)[1]
        new_file_name = file_name_no_ext + "(" + str(i) + ")" + "." + file_name_ext
        i += 1
        
        
        if os.path.exists(destination_path + "/" + new_file_name):
            file_renamer(file_name, i)
        
        try:
            shutil.move(destination_path + "/" + file_name, destination_path + "/" + new_file_name)
        except IOError:
            pass
    
    if os.path.exists(destination_path + "/" + file_name):
        file_renamer(file_name, i)
    
    
    shutil.copy2(full_path + file_name, destination_path)
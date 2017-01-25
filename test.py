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

search_directory = '/home/ubuntu/workspace/testdir'

clean_directory = '/home/ubuntu/workspace/clean/'

map_file_path = "/home/ubuntu/workspace/clean/map.txt"


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


class static:
    number = 0



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
    
    
    # def recur(new_file_name, static_number):
    #     # print(os.path.exists(destination_path + "/" +new_file_name))
    #     # print(destination_path + "/" + new_file_name)
    #     i = static_number
    #     old_file_name = new_file_name
    #     # print("destination_path + '/' + new_file_name:  " + destination_path + "/" + new_file_name)
    #     if os.path.exists(destination_path + "/" + new_file_name):  # Just a second check for safe keeping
    #         # print("yes, ", new_file_name)
    #         file_name_no_ext = file_name.split(".", 1)[0]  # creates the variable that will contain only the file name with no extension
    #         file_name_ext = file_name.split(".", 1)[1]  # Creates the variable that will contain only the file extension
    #         new_file_name = file_name_no_ext + "(" + str(i) + ")" + "." + file_name_ext  # Creates the new file name with an addition of "(#)" where the # is a number starting with 1
    #         i += 1
            
    #         # sleep(5)
    #         shutil.move(destination_path + "/" + file_name, destination_path + "/" + new_file_name)
    #         # print("Moving: " + destination_path + "/" + file_name + "  to:  " + destination_path + "/" + new_file_name + "\n\n")
    #         # sleep(5)
            
    #         # shutil.move(full_path + file_name, full_path + new_file_name)
    #         # print("Moving: " + full_path + file_name + "  to:  " + full_path + new_file_name + "\n\n")
            
    #         full_name_list.append(full_path)
    #         # print("New full_name_list")
    #         # print(full_name_list)
    #         # print("\n\n")
            
    #         file_name_list.append(new_file_name)
    #         # print("New file_name_list")
    #         # print(file_name_list)
    #         # print("\n\n")
            
    #         # sleep(5)
    #         # print("Second if:  destination_path + '/' + old_file_name: " + destination_path + "/" + old_file_name + " == " + str(os.path.exists(destination_path + "/" + old_file_name)) +  "\n\n")
    #         # sleep(5)
            
    #         # if os.path.exists(destination_path + "/" + old_file_name) and old_file_name != file_name:
    #         #     recur(old_file_name, i)
            
    #         # pass

    
    # # recur(new_file_name, static.number)
    
    # if os.path.exists(destination_path + "/" + file_name):
    #     recur(file_name, static.number)
    
    # print(new_file_name)
    
    # print("Copying  " + full_path + file_name + "  to  " + destination_path + "\n\n")
    
    
    # try:
    #     shutil.copy2(full_path + file_name, destination_path)
    # except IOError as e:
    #     pass



# map_file_read = open(map_file_path, 'r')


# for line in map_file_read:
#     line = line.strip("\n")
# # TODO: Need to make sure that if there are multiple files with the same name that they get changed so that it doesn't overwrite the files
#     if line[-3] == ".":
#         destination_path = clean_directory + line[-2:]
#     elif line[-4] == ".":
#         destination_path = clean_directory + line[-3:]
#     elif line[-5] == ".":
#         destination_path = clean_directory + line[-4:]
    
#     if not os.path.exists(destination_path):
#         os.makedirs(destination_path)
    
#     shutil.copy2(line, destination_path)
    

# map_file_read.close()




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

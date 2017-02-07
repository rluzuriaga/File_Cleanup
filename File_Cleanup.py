"""
Author: Rodrigo Luzuriaga
Date started: 01/04/2017
Date last modified: 02/06/2017

This script was created to clean up an external hard drive with data scattered all over the place.
The user, in this file, specifies the directory to where all the files are located and then creates folders for the
	file extension of all the files in the directory and all the sub-directories.
The program then copies or moves the files into the new directory that the program made for those specific files.
"""

import os
import shutil
from time import sleep

search_directory = 'C:/Users/RodrigoLuzuriaga/Desktop/aaa/'  # If working on Windows, insert directory location like this line
# search_directory = '/home/ubuntu/workspace/testdir'  # This is the directory that you want to read from. Only change what is inside the ' '

clean_directory = 'C:/Users/RodrigoLuzuriaga/Desktop/bbb/'
# clean_directory = '/home/ubuntu/workspace/clean/'  # This is the directory that you want to move the files to. In this directory the script will create all the necesary folders and copy over the files

map_file_path = 'C:/Users/RodrigoLuzuriaga/Desktop/map.txt'
# map_file_path = "/home/ubuntu/workspace/clean/map.txt"

remove_old_files_after_move = False  # For a lack of a better variable name, this just decides if the files are moved or copied
									# Make this variable False if you want the files to be copied (meaning it keeps the original files in place)
									# Make this variable True if you want the file to be moved (meaning they will be removed from the original place)











###########################################################################################################################################################################
###########################################################################################################################################################################
##
### DO NOT CHANGE ANYTHING BELLOW, UNLESS YOU KNOW WHAT YOU ARE DOING
##
###########################################################################################################################################################################
###########################################################################################################################################################################







map_file_write = open(map_file_path, 'w')  # Opening file that contains all the the information of where the file was moved from and to



full_name_list = []

file_name_list = []


for folderName, subFolders, fileNames in os.walk(search_directory):  # The function os.walk() gives out three variables while it is "walking" through the directory
	for fileName in fileNames:
		if folderName == clean_directory:
			pass
		else:
			# Append to two lists with folderName and fileName
			full_name_list.append(folderName + "/")
			file_name_list.append(fileName)



for full_path, file_name in zip(full_name_list, file_name_list):  # Iterates through two lists and gives two variables from the two lists
	counter = 1

	#
	## Checks where the dot is that starts the file extension, then creates a variable with the name of the extension. Ex. mp3, jpg, etc.
	if file_name[-3] == ".":
		destination_path = clean_directory + file_name[-2:]
	elif file_name[-4] == ".":
		destination_path = clean_directory + file_name[-3:]
	elif file_name[-5] == ".":
		destination_path = clean_directory + file_name[-4:]

	#
	## Checks if a folder with the above variable is already in the destination, clean, directory. If there is not folder with that name it creates it.
	if not os.path.exists(destination_path):
		os.makedirs(destination_path)

	m_f_n = ""
	def file_renamer(file_name, counter, m_f_n):
		r_m_f_n = ""  # Since this function is recursive, this variable has to be created to be the output of the recursive part of the function

		file_name_no_ext = file_name.split(".", 1)[0]  # Creates variable that only holds the file name without the file extension

		file_name_ext = file_name.split(".", 1)[1]  # Creates variable that holds the file name extension

		new_file_name = file_name_no_ext + "(" + str(counter) + ")" + "." + file_name_ext  # Creates the new file name that adds the file name without the extension and a number starting from 0 in paranthesis and then adds the the file extension after a dot

		counter += 1


		if os.path.exists(destination_path + "/" + new_file_name):  # Checks if this new file name is already in the new directory

			r_m_f_n = file_renamer(file_name, counter, m_f_n)  # Runs the function again using the original file name and the new number that is incremented by one every time this function runs
																# If this function runs (inside the actual function) then it outputs a variable that is checked bellow

		try:
			shutil.move(destination_path + "/" + file_name, destination_path + "/" + new_file_name)
		except IOError:  # The only time that the IOError exception should happen is when the shutil.move() function is trying to rename a file that is not there.
			pass  # If the exception does happen, then the current state of the for loop ends

		if r_m_f_n == "":  # Checks if the function only ran once, if it ran once then the variable is an empty string
			m_f_n = new_file_name  # When the function only runs once then the variable that will be returned will be the new_file_name
		else:  # If the the function is ran more than once then the output of the second (or above) time the function is ran will be returned
			m_f_n = r_m_f_n

		return m_f_n

	#
	# Checks if a file name is already in the destination folder
	# If there is a file with the name in the folder then it runs the function to change the name of that file
	if os.path.exists(destination_path + "/" + file_name):
		modified_file_name = file_renamer(file_name, counter, m_f_n)

	#
	# This just checks if the user wants to move or copy the files over and executes the right command for that
	if not remove_old_files_after_move:
		shutil.copy2(full_path + file_name, destination_path)
	elif remove_old_files_after_move:
		shutil.move(full_path + file_name, destination_path)
	else:
		print("Please make the variable 'remove_old_files_after_move' either True or False.\n")

	#
	# Checks if the output of the function 'file_renamer' is empty. If it is then it makes the variable 'modified_file_name' == file_name
	try:
		if modified_file_name == "":
			modified_file_name = file_name
	except NameError:  # If the function 'file_renamer' does not run then the variable 'modified_file_name' does not exists and this creates it
		modified_file_name = file_name

	#
	# Writes to the map file the with each line containing full path of where the file came from and where it was moved to
	map_file_write.write("Moving:  " + full_path + file_name + "  --  To:  " + destination_path + "/" + modified_file_name + "\n\n")

map_file_write.close()

# TODO: Make script detect if the file name already has a number in parentheses so that it names it in a different way.
# TODO: Check for repeated files and delete if needed (maybe make a prompt to appear to ask user) use the os.stat().st_size function to check for size if two files match the same size etc.

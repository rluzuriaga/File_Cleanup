# import time
# start_time = time.time()
"""
Author: Rodrigo Luzuriaga
Date Started: 01/04/2017
Date last modified: 02/06/2017

This script was created to clean up an external hard drive with data scattered all over the place.
The user, in this file, specifies the directory to where all the files are located and then creates folders for the
    file extension of all the files in the directory and all the sub-directories.
The program then copies or moves the files into the new directory that the program made for those specific files.
"""

import os
import shutil


def lists_creation(file_path, directory_to_original_files, list_of_original_path, list_of_file_names):
    """

    :param file_path:
    :param directory_to_original_files:
    :param list_of_original_path:
    :param list_of_file_names:
    :return:
    """

    opened_map_file = open(file_path, 'w')

    for folderName, subFolder, fileNames in os.walk(directory_to_original_files):
        for fileName in fileNames:
            if folderName in fileNames:
                pass
            else:
                list_of_original_path.append(folderName + "/")
                list_of_file_names.append(fileName)

    return opened_map_file


def destination_path_creation(listed_file_name, writing_to_directory):
    """

    :param listed_file_name:
    :param writing_to_directory:
    :return:
    """

    destination_path = ""

    if listed_file_name[-3] == ".":
        destination_path = writing_to_directory + listed_file_name[-2:]
    elif listed_file_name[-4] == ".":
        destination_path = writing_to_directory + listed_file_name[-3:]
    elif listed_file_name[-5] == ".":
        destination_path = writing_to_directory + listed_file_name[-4:]
    else:  # For files that don't have a file extension
        destination_path = writing_to_directory + "MISCELLANEOUS"

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    return destination_path


def file_renamer(destination_path, listed_file_name, counter, modified_file_name):
    """

    :param destination_path:
    :param listed_file_name:
    :param counter:
    :param modified_file_name:
    :return:
    """
    recurred_modified_file_name = ""

    file_name_no_ext = listed_file_name.split(".", 1)[0]

    try:
        file_name_ext = listed_file_name.split(".", 1)[1]
    except IndexError:  # When file doesn't have extension
        file_name_ext = None

    try:
        new_file_name = file_name_no_ext + "(" + str(counter) + ")" + "." + file_name_ext
    except TypeError:  # When file doesn't have extension
        new_file_name = file_name_no_ext + "(" + str(counter) + ")"

    counter += 1

    if os.path.exists(destination_path + "/" + new_file_name):
        recurred_modified_file_name = file_renamer(destination_path, listed_file_name, counter, modified_file_name)

    try:
        shutil.move(destination_path + "/" + file_name, destination_path + "/" + new_file_name)
    except IOError:
        pass

    if recurred_modified_file_name == "":
        modified_file_name = new_file_name
    else:
        modified_file_name = recurred_modified_file_name

    return modified_file_name


def keeping_old_files_decision(keep_old_files, destination_path):
    """

    :param keep_old_files:
    :param destination_path:
    :return:
    """
    if not keep_old_files:
        shutil.copy2(full_path + file_name, destination_path)
    elif keep_old_files:
        shutil.move(full_path + file_name, destination_path)
    else:
        print("Please make the variable 'remove_old_files_after_move' either True or False.\n")


def map_file_writer(modified_file_name, listed_file_name, map_file_write, destination_path):
    """

    :param modified_file_name:
    :param listed_file_name:
    :param map_file_write:
    :param destination_path:
    :return:
    """
    try:
        if modified_file_name == "":
            modified_file_name = listed_file_name
    except NameError:
        modified_file_name = listed_file_name

    map_file_write.write(
        "Moving:  " + full_path + file_name + "  --  To:  " + destination_path + "/" + modified_file_name + "\n\n")


if __name__ == "__main__":

    # search_directory = 'C:/Users/RodrigoLuzuriaga/Downloads/'
    search_directory = '/home/rluzuriaga/Desktop/'

    # clean_directory = 'C:/Users/RodrigoLuzuriaga/Desktop/downloads/'
    clean_directory = '/home/rluzuriaga/test/'

    # map_file_path = 'C:/Users/RodrigoLuzuriaga/Desktop/map.txt'
    map_file_path = '/home/rluzuriaga/map.txt'

    remove_old_files_after_move = False

    full_name_list = []

    file_name_list = []

    map_file = lists_creation(map_file_path, search_directory, full_name_list, file_name_list)

    for full_path, file_name in zip(full_name_list, file_name_list):
        counter = 1

        full_path_of_destination = destination_path_creation(file_name, clean_directory)

        modified_file_name = ""

        if os.path.exists(full_path_of_destination + "/" + file_name):
            modified_file_name = file_renamer(full_path_of_destination, file_name, counter, modified_file_name)

        keeping_old_files_decision(remove_old_files_after_move, full_path_of_destination)

        map_file_writer(modified_file_name, file_name, map_file, full_path_of_destination)

    map_file.close()
# TODO: make files with multiple "." in the file name work (currently they don't)

# print(time.time() - start_time)

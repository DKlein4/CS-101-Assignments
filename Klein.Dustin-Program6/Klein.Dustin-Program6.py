'''
CS 101
Klein.Dustin-Program6
Assignment 6
Dustin Klein
dbktgb@mail.umkc.edu
Problem: Split multiple ppm pictures into slices and combine them
Algorithm:
•	Ask user for source
•	Ask the user for output name
•	Check files in the source folder
o	Correct size
o	Correct header
•	Slice the photographs together
o	Total number of files is the number of slices
o	Width of each slice = total width and divide by number of files
o	Take out the appropriate section of each photo
	The first is just from 0 – width
	Second is form width – 2width
	And so on
o	Combine all those slices into the output file
'''
import os

def getFiles():
    #Asks for the directory that contains the files, validates that it contains valid files, then returns a list of open files.

    valid_source = False
    while not valid_source:
        try:
            #get the name of the directory
            source_name = input("\nEnter a directory that contains valid image files ==> ")
            source = os.chdir(source_name)
        except:
            print("Directory could not be opened.\n")
            continue

        file_list = []  # will be used as a list of open files
        name_list = os.listdir(source)  # list of the names of the files in the directory
        ppm_list = [x for x in name_list if x[-4:] == ".ppm"]  # list of the ppm files in the directory

        # opens the ppm files and stores them in file_list
        try:
            for f in ppm_list:
                F = open(f)
                file_list.append(F)
        except:
            print("Could not open files")
            continue

        first_line_list = []
        dimensions_list = []
        depth_list = []

        # store each of the first three lines from each document
        for f in file_list:
            for i in range(4):
                if i == 1:
                    line = f.readline()
                    first_line_list.append(line)
                if i == 2:
                    line = f.readline()
                    dimensions_list.append(line)
                if i == 3:
                    line = f.readline()
                    depth_list.append(line)

        print()  # formatting

        # check that each document's first line is P3

        valid_first_lines = False
        for i in range(4):
            if first_line_list[i] != "P3\n":
                print(ppm_list[i - 1], "first line is not P3")
                valid_first_lines = False
            else:
                valid_first_lines = True


        # check that all of the dimensions match
        valid_dimensions = False
        for i in range(4):
            for j in range(i + 1, 4):
                if dimensions_list[i] != dimensions_list[j]:
                    print(ppm_list[i - 1], "does not match the dimensions of", ppm_list[j - 1])
                    valid_dimensions = False
                else:
                    valid_dimensions = True

        # check that the bit depth is 255
        valid_depths = False
        for i in range(4):
            if int(depth_list[i]) != 255:
                print(ppm_list[i - 1], "does not have a bit depth of 255")
                valid_depths = False
            else:
                valid_depths = True

        # if all of those are true, everythings good
        if valid_first_lines and valid_dimensions and valid_depths:
            valid_source = True

            dimensions = dimensions_list[0]
            dimensions = dimensions.split()
            dimensions = [int(x) for x in dimensions]

            return file_list, dimensions

def getOutputFile():
    #Gets the name of the ouput file from the user

    valid_name = False
    while not valid_name:
        try:
            file_name = input("\nEnter the file to save the ppm to. ==> ")
            file = open(file_name, "w")
            valid_name = True
        except OSError:
            print("Unable to open that file.\n")

    return file

def closeFiles(files):
    #Takes in a list of open files and closes them all

    for f in files:
        f.close()

def splitFiles(f, o, d):
    #splits the files

    files = f
    out = o
    dimensions = d

    print("P3", file = out)
    print(dimensions[0], dimensions[1], file = out)
    print("255", file = out)

    num_files = len(files)
    width_of_splits = dimensions[0] / num_files

    num_row = dimensions[0]
    num_col = dimensions[1]
    length = dimensions[0] * dimensions[1]

    # for row in range(num_col):
    #     for i in range(len(files)):
    #         for j in range(int(width_of_splits)):
    #             readPixel(files[i], out)

    for row in range(num_row):
        for i in range(num_files):
            for j in range(int(width_of_splits)):
                readPixel(files[i], out, i)

def readPixel(f, o, i):
    #Reads three lines which is the equivalent of a pixel

    file = f
    out = o
    inc = i

    while inc > 1:
        for i in range(3):
            file.readline()

        inc -= 1

    for i in range(3):
        line = file.readline()
        out.write(line)


file_list, dimensions = getFiles()
# print(file_list)
output = getOutputFile()
splitFiles(file_list, output, dimensions)
closeFiles(file_list)

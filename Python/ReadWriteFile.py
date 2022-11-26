# Demonstrates basic file operations in python
#   - Reads a text file and writes content of file to stdout
#   - TODO: Reads a text file and writes content of file into an output file
#
# Created By: Josh Johnson

from os import path

# reading a basic file and printing contents to stdout
# get current directory location of ReadWriteFile.py
base_path = path.dirname(__file__)

# relative path to the test file basic_text.txt
file_path = path.abspath(path.join(base_path, "..", "Test_Files", "basic_text.txt"))

# opening basic_text.txt
file1 = open(file_path, "r")

# reading data from file stored in file1 and storing it in data
data = file1.read()

# closing the file located in the variable file1
file1.close()

# printing info stored in file1 to stdout
print(data)

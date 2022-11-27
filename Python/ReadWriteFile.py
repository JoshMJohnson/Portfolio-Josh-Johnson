# Demonstrates basic file operations in python
#   - Reads a text file and writes content of file to stdout
#   - Reads a text file and writes content of file into an output file
#
# Created By: Josh Johnson

from os import path # used to get relative path for input text files

# get current directory location of ReadWriteFile.py
base_path = path.dirname(__file__)

# *** reads a text file and writes content of file to stdout ***
# relative path to the test file
file_path = path.abspath(path.join(base_path, "..", "Test_Files", "basic_text.txt"))

# open access to test file
file1 = open(file_path, "r")

# reading from variable storing access to the test file and saving its content
data = file1.read()

# closing the file access to test file
file1.close()

# printing data stored from reading file to stdout
print(data)

# *** reads a text file and writes content of file into an output file ***
# relative path to the test file
file_path = path.abspath(path.join(base_path, "..", "Test_Files", "poem.txt"))

# open access to test file
file1 = open(file_path, "r")

# reading from variable storing access to the test file and saving its content
data = file1.read()

# closing the file access to test file
file1.close()

# relative path to the output file
file_path = path.abspath(path.join(base_path, "Output_Files", "poem_dup_from_readwritefile.txt"))

# creates output file access
file2 = open(file_path, "w")

# write content from test file to output file
file2.write(data)

# closing the file access to the output file
file2.close()
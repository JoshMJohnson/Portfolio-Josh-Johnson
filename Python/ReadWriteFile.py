# Demonstrates basic file operations in python
#   - Reads a text file and writes content of file to stdout
#   - TODO: Reads a text file and writes content of file into an output file
#
# Created By: Josh Johnson

from os import path

# get current directory location of ReadWriteFile.py
base_path = path.dirname(__file__)

# *** reads a text file and writes content of file to stdout ***
# relative path to the test file
file_path = path.abspath(path.join(base_path, "..", "Test_Files", "basic_text.txt"))

# open text file
file1 = open(file_path, "r")

# reading from variable storing access to the text file and saving its content
data = file1.read()

# closing the file access
file1.close()

# printing info stored in file1 to stdout
print(data)



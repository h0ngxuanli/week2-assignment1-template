# This script has partial code that is part of the bonus challenge of the lesson. The goal is to get you to think about how to use functions and classes which you've 
# learned already to solve a problem. This challenge is very similar to that of week 1 with the added requirements of functions and classes.
# Use the comments in the code as guidance to complete the challenge.
# Objectives: In this challenge you will need to capture information from files (again!).
# Objectives:
# 1. Use the provided code to iterate (loop) over every file in a path (defaults to current directory)
# 2. Capture the file name and the size of the file in a dictionary
# 3. Print out the file name and size of the file in a human readable format sorting from largest to smallest file size
# 4. No code (aside from `path`) should be outside of a function or class!

# Note: Run this script on the root of the repository and pass in a path as an argument. For example: `python bonus/main.py /tmp`

import os
import sys

# Don't move this variable!
# Path to the directory to iterate over, fallsback to current directory
path = sys.argv[1] if len(sys.argv) > 1 else '.'

# Modify this class so that it formats bytes into different human readable formats
# like MB, KB, and GB
class FileSize:

    def __init__(self, bytes):
        self.bytes = bytes

    def MB(self):
        pass

    def KB(self):
        pass

    def GB(self):
        pass


# Modify this function so that it sorts the dictionary by file size. The trick here is to return a list of tuples instead of a dictionary so that
# the order is preserved
def sort_by_size(file_sizes):
    pass


# TODO: Move this to the main() function
# Dictionary to hold the file name and size
file_sizes = {}

# TODO: Make this a function that takes a path as an argument and returns a dictionary of file names and sizes
# Iterate over the files in the directory
for root, dirs, files in os.walk(path):
    for file in files:
        # Get the full path to the file
        full_path = os.path.join(root, file)

        # Use the os.path.getsize function to get the file size

        # Add the file size to the dictionary

# TODO: Move this to the main() function. 
# Modify the following code to print out the file sizes in a human readable format, sorted by largest to smallest
# Note that the current code will only print out the filename and nothing else.
for file in file_sizes:
    print(f"File: {file}")


# Make this function your main function (main entry point) where all the logic happens
def main():
    pass


# This is used to run the main function when the script is executed
if __name__ == '__main__':
    main()

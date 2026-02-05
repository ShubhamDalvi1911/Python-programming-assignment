"""
Count Lines in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many lines are present in the file.
"""
import os
def count_lines_in_file(file_name):
    if os.path.exists(file_name):

        fobj = open(file_name, "r")
        count = 0
        for line in fobj:       # line = "Jay Ganesh..."
            count = count + 1   # count = count + 1
        fobj.close()
        print(f"Number of lines in the file: {count}")
    else:
        print("File not found.")
    
def main():
    file_name = input("Enter the file name: ")
    count_lines_in_file(file_name)
    

if __name__ == "__main__":
    main()
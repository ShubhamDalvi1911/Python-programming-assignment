"""
Display File Line by Line
Problem Statement:
Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
"""
import os
def display_line_by_line(file_name):
    if os.path.exists(file_name):

        fobj = open(file_name, "r")
        data = fobj.read()
        print(data)
        # for line in fobj:              
        #     print(line)
        fobj.close()
    else:
        print("File not found.")
    
def main():
    file_name = input("Enter the file name: ")
    display_line_by_line(file_name)
    
if __name__ == "__main__":
    main()
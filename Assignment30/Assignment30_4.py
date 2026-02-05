"""
Copy File Contents into Another File
Problem Statement:
write a program which accepts two file names from the user.
  - First file is an existing file
  - Second file is a new file
copy all contents from the first file into the second file.
"""
import os
def Copy_File(file_name):
    if os.path.exists(file_name):

        fobj = open(file_name, "r")
        data = fobj.read()
        fobj.close()

        file_name2 = input("Enter the new file name: ")
        
        fobj1 = open(file_name2, "w")
        fobj1.write(data)
        fobj1.close()

        print("File copied successfully.")

    else:
        print("File not found.")
    
def main():
    file_name1 = input("Enter the existing file name: ")
    Copy_File(file_name1)
    
if __name__ == "__main__":
    main()
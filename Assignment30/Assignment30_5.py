"""
Search a word in File
Problem Statement:
write a program which accepts two file names and a word from the user and checks whether that word is present in the file or not.
"""
import os
def Search_word(file_name , word):
    if os.path.exists(file_name):
        fobj = open(file_name, "r")
        data = fobj.read()
        fobj.close()

        if word in data:
            print(f"Word '{word}' is present in the file.")
        else:
            print(f"Word '{word}' is not present in the file.")
        

    else:
        print("File not found.")
    
def main():
    file_name1 = input("Enter the existing file name: ")
    word = input("Enter the word to search: ")
    Search_word(file_name1 , word)
    
if __name__ == "__main__":
    main()
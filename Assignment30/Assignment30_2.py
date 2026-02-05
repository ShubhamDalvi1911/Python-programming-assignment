"""
Count Words in a File
Problem Statement:
Write a program which accepts a file name from the user and counts how many words are present in the file.
"""
import os
def count_words_in_file(file_name):
    if os.path.exists(file_name):

        fobj = open(file_name, "r")
        count = 0
        for line in fobj:               # line = "Jay Ganesh..."
            words = line.split()        # split the line into words and store in list ["Jay", "Ganesh..."]
            count = count + len(words)  # count = count + 2
        fobj.close()
        print(f"Number of words in the file: {count}")
    else:
        print("File not found.")
    
def main():
    file_name = input("Enter the file name: ")
    count_words_in_file(file_name)
    

if __name__ == "__main__":
    main()
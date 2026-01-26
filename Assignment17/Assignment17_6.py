# Write a program which accept one number and display below pattern
'''
Enter a number : 5
 *  *  *  *  * 
 *  *  *  *
 *  *  *
 *  *
 *
'''
def Pattern(No):
    for i in range(No):
        for j in range(i+1,No+1):
            print(" * ", end='')
        print()


def main():
    No = int(input("Enter a number : "))
    Pattern(No)
    

if __name__ == "__main__":
    main()
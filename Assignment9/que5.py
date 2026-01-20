#write a program which accepts one number and checks wheather it is divisible by 3 and 5
def divisible(No):
    if (No % 3) == 0 and (No % 5) == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    No = int(input("Enter a number you want check : "))
    divisible(No)
    
if __name__ == "__main__":
    main()
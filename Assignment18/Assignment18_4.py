# Write a program whcih accept N numbers from user and store it into list. Accept one another number from user and return frequency of that number from list.

def FrequencyOfNum(num_list,No):
    Freq = 0
    for i in num_list:
        if i == No:
            Freq = Freq + 1
            
    return Freq

def main():
    num = int(input("Enter how many numbers you want to enter: "))
    num_list = []
    for i in range(num):
        No = int(input(f"Enter number {i+1} :"))
        num_list.append(No)

    No = int(input("Enter number to find frequency: "))
    result = FrequencyOfNum(num_list,No)
    print("Frequency of number is ", result)

if __name__ == "__main__":
    main()
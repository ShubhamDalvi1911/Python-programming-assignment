# Write a program whcih accept N numbers from user and store it into list. Return addition of all elements from that list.

def SumOfElements(num_list):
    sum = 0
    for i in num_list:
        sum = sum + i
    return sum

def main():
    num = int(input("Enter how many numbers you want to enter: "))
    num_list = []
    for i in range(num):
        No = int(input(f"Enter number {i+1} :"))
        num_list.append(No)

    result = SumOfElements(num_list)
    print("Addition of all elements is:", result)

if __name__ == "__main__":
    main()
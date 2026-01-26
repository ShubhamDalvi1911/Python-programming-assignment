# Write a program whcih accept N numbers from user and store it into list. Return maximum number from that list.

def MaxOfElements(num_list):
    max = 0
    for i in num_list:
        if i > max:
            max = i

    return max

def main():
    num = int(input("Enter how many numbers you want to enter: "))
    num_list = []
    for i in range(num):
        No = int(input(f"Enter number {i+1} :"))
        num_list.append(No)

    result = MaxOfElements(num_list)
    print("Maximum number is:", result)

if __name__ == "__main__":
    main()
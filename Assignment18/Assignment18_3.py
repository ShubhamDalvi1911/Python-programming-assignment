# Write a program whcih accept N numbers from user and store it into list. Return minimum number from that list.

def MinOfElements(num_list):
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
            
    return min

def main():
    num = int(input("Enter how many numbers you want to enter: "))
    num_list = []
    for i in range(num):
        No = int(input(f"Enter number {i+1} :"))
        num_list.append(No)

    result = MinOfElements(num_list)
    print("Minimum number is ", result)

if __name__ == "__main__":
    main()
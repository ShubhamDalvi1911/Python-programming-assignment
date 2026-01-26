# Write a program which contains one lambda function which accepts one parameter and return power of two

power_of_two = lambda x: x * x

def main():
    number = int(input("Enter a number: "))
    result = power_of_two(number)
    print(f"The power of two of {number} is {result}")

if __name__ == "__main__":
    main()
# Write a program which accepts one number and prints count of digits in that number
def CountOf(No):
    count = 0
    for dig in No:
        count = count + 1
    return count

def main():
    No = 0
    result = 0
    No = int(input("Enter a number : "))
    result = CountOf(str(No))
    print(result)

if __name__ == "__main__":
    main()
# Write a program whcih accepts one number and prints its factors.
def factor(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i , end=' ')

def main():
    No = int(input("Enter a number : "))
    result = factor(No)

if __name__ == "__main__":
    main()
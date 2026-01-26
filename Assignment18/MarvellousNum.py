def prime(No):
    if No == 1:
        print("1 is nither prime nor composit")
    else:
        for i in range(2,No//2+1):
            if (No % i) == 0:
                return False
        else:
            return True
            
def main():
    No = 0
    No = int(input("Enter a number : "))
    prime(No)


if __name__ == "__main__":
    main()
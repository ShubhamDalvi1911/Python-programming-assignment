# Write a program which accepts one number and checks whether it prime or not
def prime(No):
    if No == 1:
        print("1 is nither prime nor composit")
    else:
        for i in range(2,No//2):
            if No%i == 0:
                print("Not prime Number")
                break
        else:
            print("Prime Number")
                

def main():
    No = 0
    No = int(input("Enter a number : "))
    prime(No)

if __name__ == "__main__":
    main()
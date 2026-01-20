# Write a program whcih accepts two number and prints its addition , substraction , multiplication and division
def Calculation(No1, No2):
    add = No1 + No2
    sub = No1 - No2
    mul = No1 * No2
    div = No1 / No2
    return add , sub , mul , div    

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    result = Calculation(No1, No2)
    print("addition , substraction , multiplication and division of two number is : ",result)

if __name__ == "__main__":
    main()
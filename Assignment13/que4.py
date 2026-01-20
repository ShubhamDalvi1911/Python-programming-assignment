# Write a program which accepts one number and prints binary equivalent
def Bequivalent(No):
    reminder = ''
    while No != 0:
        rem = No // 2
        reminder = reminder + str(No%2) 
        No = rem
    return reminder


def main():
    No = int(input("Enter a number : "))
    result = Bequivalent(No)        # 11101
    str_result = int((result)[::-1])   # '11101'
    print(str_result)
    
if __name__ == "__main__":
    main()
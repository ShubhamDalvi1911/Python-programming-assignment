# Write a program which accept name from user and display length of its name.
def NameLen(name):
    return len(name)

def main():
    Name = input("Enter your name and get lenght of it : ")
    result = NameLen(Name)
    print(result)


if __name__ == "__main__":
    main()
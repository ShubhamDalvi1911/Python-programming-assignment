# Write a lambda function using filter() which accepts a list of strings and returns the list of strings having length grater than 5
GreaterString = lambda string : len(string) > 5

def main():
    strings = list()
    no = int(input("Enter how many strings you want to store : "))
    for i in range(no):
        print("Enter", i+1 ," string : ", end='')
        strings.append(input())

    result = list(filter(GreaterString,strings))

    print("strings having length grater than 5 ",result)


if __name__ == "__main__":
    main()